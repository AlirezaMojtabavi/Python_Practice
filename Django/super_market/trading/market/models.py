from django.db import models, IntegrityError
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError


def positive_validate(value):
    if value < 0:
        raise ValidationError(
            ('Quantity %(value)s is not allowed'),
            params={'value': value},
        )


class Product(models.Model):
    code = models.CharField(max_length=10, unique=True,
                            error_messages={"unique": "This code has already been registered."}, null=False)
    name = models.CharField(max_length=100, null=False)
    price = models.PositiveIntegerField(validators=[positive_validate], null=False)
    inventory = models.PositiveIntegerField(default=0, validators=[positive_validate])

    def increase_inventory(self, amount):
        if amount <= 0:
            raise ValueError("amount must be greater than zero")
        else:
            self.inventory += amount
            self.save()

    def decrease_inventory(self, amount):
        if amount <= 0:
            raise ValueError("amount must be greater than zero")
        else:
            self.inventory -= amount
            if self.inventory < 0:
                raise ValueError("inventory of the %s is not enough" % self.name)
            else:
                self.save()

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True)
    address = models.TextField()
    balance = models.PositiveIntegerField(default=20000, validators=[positive_validate])

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be greater than zero")
        else:
            self.balance += amount
            self.save()

    def spend(self, amount):
        if amount <= 0:
            raise ValueError("amount must be greater than zero")
        else:
            self.balance -= amount
            if self.balance < 0:
                raise ValueError("Credit is not enough")
            else:
                self.save()


class OrderRow(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='rows')
    amount = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(90000)], null=False)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_time = models.DateTimeField(default=datetime.now())
    total_price = models.IntegerField(default=0)
    STATUS_SHOPPING = 1
    STATUS_SUBMITTED = 2
    STATUS_CANCELED = 3
    STATUS_SENT = 4
    choice_status = (
        (STATUS_SHOPPING, 'در حال خرید'),
        (STATUS_SUBMITTED, 'ثبت‌شده'),
        (STATUS_CANCELED, 'لغوشده'),
        (STATUS_SENT, 'ارسال‌شده'),
    )
    status = models.IntegerField(choices=choice_status)

    @staticmethod
    def initiate(customer):
        order_customer = Order.objects.filter(customer_id=customer.id)
        flag = False
        for item in order_customer:
            if item.status == 1:
                flag = True
                return item
            else:
                continue

        if not flag:
            order = Order()
            order.status = 1
            order.customer_id = customer.id
            order.save()
            return order

    def add_product(self, product, amount):
        if amount <= 0 or self.status > 1:
            raise ValueError("amount must be greater than zero and check status")
        else:
            self.status = 1
            p = Product.objects.get(id=product.id)
            if amount > p.inventory:
                self.status = 1
                raise ValueError("The inventory of the product is not enough!")

            elif p.price * amount > self.customer.balance:
                self.status = 1
                raise ValueError("Balance of the Customer is not enough")

            else:
                self.status = 1
                self.rows.create(product_id=p.id, order_id=self.id, amount=amount)
                p.decrease_inventory(amount)
                self.customer.spend(amount * p.price)
                self.total_price += amount * p.price
                self.save()

    def remove_product(self, product, amount=None):
        if self.status == 1:
            p = Product.objects.get(id=product.id)
            row = self.rows.get(product_id=p.id, order_id=self.id, order__customer_id=self.customer.id)
            amount_of_row = row.amount
            if (amount is None) or (amount == amount_of_row):
                p.increase_inventory(amount_of_row)
                self.customer.deposit(p.price * amount_of_row)
                self.total_price -= p.price * amount_of_row
                row.delete()
                self.save()

            elif (amount >= 1) and (amount < amount_of_row):
                p.increase_inventory(amount)
                self.customer.deposit(p.price * amount)
                self.total_price -= p.price * amount
                row.amount -= amount
                row.save()
                self.save()
            else:
                raise ValidationError("Invalid value for amount")
        else:
            raise ValidationError("For using 'remove_product', status must be 1")

    def submit(self):
        if self.status == 1:
            self.status = 2
            self.save()
        else:
            raise ValidationError("For using 'submit', status must be 1")

    def cancel(self):
        if self.status == 2:
            rows = self.rows.filter(order_id=self.id, order__customer_id=self.customer.id)
            for row in rows:
                p = Product.objects.get(id=row.product_id)
                amount = row.amount
                self.customer.deposit(p.price * amount)
                p.increase_inventory(amount)
                self.total_price -= p.price * amount
                row.delete()

            self.status = 3
            self.save()
        else:
            raise ValidationError("For using 'cancel', status must be 2")

    def send(self):
        if self.status == 2:
            self.status = 4
            self.save()
        else:
            raise ValidationError("For using 'send', status must be 2")

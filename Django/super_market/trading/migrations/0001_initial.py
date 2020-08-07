# Generated by Django 3.0.6 on 2020-06-18 04:25

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import trading.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, null=True)),
                ('address', models.TextField()),
                ('balance', models.PositiveIntegerField(default=20000, validators=[trading.models.positive_validate])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateTimeField(default=datetime.datetime(2020, 6, 18, 8, 55, 20, 391729))),
                ('total_price', models.IntegerField(default=0)),
                ('status', models.IntegerField(choices=[(1, 'در حال خرید'), (2, 'ثبت\u200cشده'), (3, 'لغوشده'), (4, 'ارسال\u200cشده')])),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trading.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(error_messages={'unique': 'This code has already been registered.'}, max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField(validators=[trading.models.positive_validate])),
                ('inventory', models.PositiveIntegerField(default=0, validators=[trading.models.positive_validate])),
            ],
        ),
        migrations.CreateModel(
            name='OrderRow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(90000)])),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rows', to='trading.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trading.Product')),
            ],
        ),
    ]
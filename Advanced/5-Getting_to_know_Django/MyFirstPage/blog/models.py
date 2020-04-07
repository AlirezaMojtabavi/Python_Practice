from django.db import models

# Create your models here.
class Post(models.Model):
    txt = models.CharField(max_length = 480)
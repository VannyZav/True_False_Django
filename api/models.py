from django.contrib.auth.models import AbstractUser
from django.db import models

# from api.managers import CustomUserManager


class ApiUser(AbstractUser):
    ...
    # name = models.CharField(max_length=150)
    # email = models.EmailField(unique=True)
    # phone = models.CharField(max_length=15, unique=True)
    # agrees_to_policy = models.BooleanField(default=False)
    #
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['name', 'phone']
    #
    # objects = CustomUserManager()
    #


class User(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    agrees_to_policy = models.BooleanField(default=False)
    play = models.BooleanField(default=False)


class Product(models.Model):
    name = models.CharField(max_length=128)
    firstInfo = models.CharField(max_length=256)
    secondInfo = models.CharField(max_length=256)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    exists = models.BooleanField()




from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from api.managers import CustomUserManager


class ApiUser(AbstractBaseUser):

    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    agrees_to_policy = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    objects = CustomUserManager()


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    exists = models.BooleanField




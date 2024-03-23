from django.contrib.auth.models import AbstractUser
from django.db import models


"""Модель только для суперпользователя, можно создать только через 'py manage.py createsuperuser'"""
class ApiUser(AbstractUser):
    ...


"""Модель пользователя, который играет."""
class User(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    agrees_to_policy = models.BooleanField(default=False)
    play = models.BooleanField(default=False)


"""Модель продукта."""
class Product(models.Model):
    #  id автоматическое
    name = models.CharField(max_length=128)
    firstInfo = models.CharField(max_length=256)
    secondInfo = models.CharField(max_length=256)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    exists = models.BooleanField()




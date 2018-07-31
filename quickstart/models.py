from django.db import models


# Create your models here.

class Company(models.Model):
    """docstring for Company"""
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)


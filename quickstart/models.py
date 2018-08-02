from django.db import models
from rest_framework import serializers

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
      return self.name

class Project(models.Model):
    """docstring for Company"""
    name = models.CharField(max_length=50)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
      return self.name

class Programmer(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
      return self.name
from django.db import models
from rest_framework import serializers


class Ceo(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
      return self.name


class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
      return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    ceo = models.ForeignKey(Ceo, on_delete=models.CASCADE)

    def __str__(self):
      return self.name


class Programmer(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
      return self.name

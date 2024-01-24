from django.db import models


class Animal(models.Model):
    animal = models.CharField(default='animal', max_length=50)
    kind = models.CharField(default='kind', max_length=50)
    color = models.CharField(default='color', max_length=50)

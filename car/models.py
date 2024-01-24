from django.db import models

class Car(models.Model):
    car_name = models.CharField(default='name', max_length=20)
    model = models.CharField(default='model', max_length=30)
    year = models.IntegerField(default=0)
    price = models.IntegerField(default=0)


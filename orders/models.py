from django.db import models
from django.contrib.auth.models import User
from cars.models import Car

# Create your models here.


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

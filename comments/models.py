from django.db import models
from cars.models import Car

# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

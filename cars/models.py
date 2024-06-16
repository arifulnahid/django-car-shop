from django.db import models
from brand.models import Brand

# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=15)
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField()
    price = models.IntegerField()
    qunatity = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

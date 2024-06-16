from django.contrib import admin
from . import models
# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price', 'qunatity']


admin.site.register(models.Car, CarAdmin)

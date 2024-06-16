from django.contrib import admin
from . import models

# Register your models here.


class BrandAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']


admin.site.register(models.Brand, BrandAdmin)

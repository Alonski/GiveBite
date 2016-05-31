from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Company)
admin.site.register(models.Customer)
admin.site.register(models.Dish)
admin.site.register(models.Restaurant)

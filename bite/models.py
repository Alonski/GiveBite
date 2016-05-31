from django.db import models


# Create your models here.

class Dish(models.Model):
    dish_name = models.CharField(max_length=200, )
    dish_price = models.DecimalField(max_digits=14, decimal_places=2)
    dish_desc = models.CharField(max_length=1000)

    def __str__(self):
        return "{}-{}-{}".format(self.dish_name, self.dish_price, self.dish_desc)

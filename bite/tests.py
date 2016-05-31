from django.core.urlresolvers import reverse
from django.test import TestCase
from .models import Dish

# Create your tests here.

class DefaultViewTests(TestCase):
    def test_index(self):
        response = self.client.get(reverse('bite:index'))
        self.assertEquals(response.status_code, 200)


class DishModelTests(TestCase):
    def test_create_dish_with_empty_dish_name(self):
        dish = Dish(name='', price='5', desc='Dish_Mock_Desc')
        dish.full_clean()
        dish.save()
        self.assertEquals(dish, '<Dish: -5-Dish_Mock_Desc>')


# def create_dish(dish_name, dish_price, dish_desc):
#     """
#     Create Dish for tests
#     :param dish_name: Name of new Dish
#     :param dish_price: Price of New Dish
#     :param dish_desc: Description of new Dish
#     :return: New Dish Object
#     """
#     return

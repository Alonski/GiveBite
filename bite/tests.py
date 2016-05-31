from django.core.exceptions import ValidationError
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
        dish = create_dish('', '5', 'Dish_Mock_Desc')
        self.assertRaises(expected_exception=ValidationError())
        # self.assertEquals(dish.__str__(), '-5-Dish_Mock_Desc')


def create_dish(dish_name, dish_price, dish_desc):
    """
    Create Dish for tests
    :param dish_name: Name of new Dish
    :param dish_price: Price of New Dish
    :param dish_desc: Description of new Dish
    :return: New Dish Object
    """
    dish = Dish(name=dish_name, price=dish_price,
                description=dish_desc)
    dish.full_clean()
    dish.save()
    return dish

from pprint import pprint

from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db.models import Sum
from django.test import TestCase
from .models import Dish, Restaurant, Order


# Create your tests here.

class DefaultViewTests(TestCase):
    def test_index(self):
        response = self.client.get(reverse('bite:index'))
        self.assertEquals(response.status_code, 200)


class DishModelTests(TestCase):
    # def test_create_dish_with_empty_dish_name(self):
    #     rest = create_restaurant()
    #     dish = create_dish(restaurant=rest)
    #     self.assertRaises(expected_exception=ValidationError())
    #     # self.assertEquals(dish.__str__(), '-5-Dish_Mock_Desc')

    def test_create_12_dishes(self):
        n = 12
        rest = create_restaurant()
        for i in range(n):
            dish = create_dish(restaurant=rest)
        # print(Dish.objects.count())
        self.assertEquals(Dish.objects.count(), n)


class OrderModelTests(TestCase):
    def test_orders(self):
        n = 12
        rest = create_restaurant()
        order = create_order(restaurant=rest)
        for i in range(n):
            dish = create_dish(restaurant=rest)
            order.dishes.add(dish)
        # print(Dish.objects.count())
        pprint(order.dishes.all().aggregate(sum=Sum('price'))['sum'])
        self.assertEquals(Dish.objects.count(), n)


def total(self):
    return self.get_queryset().aggregate(sum=Sum('amount'))['sum']


def create_restaurant(name="Aroma", address="Street", phone="555", email="alon@alon.com", active=True, owner="Bob", description="Aroma Desc"):
    """
    Create Restaurant for tests
    :return: New Restaurant Object
    """
    restaurant = Restaurant(name=name, address=address, phone=phone, email=email, active=active, owner=owner, description=description)
    restaurant.full_clean()
    restaurant.save()
    return restaurant


def create_dish(restaurant, dish_name="Dish Name", dish_price=5.5, dish_desc="Dish Desc"):
    """
    Create Dish for tests
    :param dish_name: Name of new Dish
    :param dish_price: Price of New Dish
    :param dish_desc: Description of new Dish
    :param restaurant: Restaurant this Dish belongs to
    :return: New Dish Object
    """
    dish = Dish(name=dish_name, price=dish_price, description=dish_desc, restaurant=restaurant)
    dish.full_clean()
    dish.save()
    return dish


def create_order(restaurant, price=0):
    """
    Create Restaurant for tests
    :return: New Restaurant Object
    """
    order = Order(restaurant=restaurant, price=price)
    order.full_clean()
    order.save()
    return order

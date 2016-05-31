from bite.models import Dish


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


d = create_dish("Tester", "5.50", "Wow")

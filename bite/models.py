import logging
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.db import models
from django.core.validators import MinValueValidator
from django.db.models import Sum
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
# TODO move this validator to somewhere else!
name_validator = RegexValidator(r'^[a-zA-Z]+$')


class Gender:
    MALE = 1
    FEMALE = 2

    choices = (
        (MALE, 'male'),
        (FEMALE, 'female'),
    )


# TODO add imagaField for restaurant image, resize it.
class Restaurant(models.Model):
    """
    Fields - Name, Address, Phone, Email, Active, Owner, Description
    """
    # Relations
    # Attributes - Mandatory
    name = models.CharField(
        max_length=30,
        # validators=[],
    )
    address = models.CharField(
        max_length=100,
        verbose_name='address',
        help_text='Enter a valid address(City, Street, Number)',
        # TODO regex validator for all languages.
        # validators=[],
    )

    # TODO regex validator for all languages.
    phone = models.CharField(
        max_length=10,
        verbose_name='phone',
        # validators=[],
        help_text='Enter a valid phone number',
    )

    email = models.EmailField(verbose_name='email')

    active = models.BooleanField(default=True)
    owner = models.CharField(max_length=30)
    # Attributes - Optional
    description = models.TextField(blank=True, null=True)
    popularity = models.PositiveIntegerField(default=0, editable=False)

    # Object Manager
    # Custom Properties Methods
    # Meta and String
    class Meta:
        verbose_name = 'restaurant'
        verbose_name_plural = 'restaurants'

    def __str__(self):
        return "{} - {}".format(self.name, self.phone)

    def get_absolute_url(self):
        return reverse('bite:restaurant_detail', args=(self.pk,))


class Dish(models.Model):
    # Relations
    restaurant = models.ForeignKey(
        Restaurant,
        related_name='dishes',
        on_delete=models.CASCADE,
    )
    # Attributes - Mandatory
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    # Attributes - Optional
    description = models.CharField(max_length=100, null=True, blank=True)

    # Object Manager
    # Custom Properties Methods
    # Meta and String

    def __str__(self):
        # if self.restaurant:
        #     return "{}-{}-{}-{}".format(self.name, self.price, self.description, self.restaurant)
        # else:
        return "{}-{}-{}".format(self.name, self.price, self.description)


# class Company(models.Model):
#     # Relations
#     restaurant = models.ManyToManyField(
#         Restaurant,
#         related_name='companies',
#         verbose_name='restaurant',
#         blank=True,
#     )
#     # Attributes - Mandatory
#     name = models.CharField(
#         max_length=30,
#         validators=[],
#     )
#     address = models.CharField(
#         max_length=100,
#         verbose_name='address',
#         help_text='Enter valid address(City, Street, Number)',
#         # TODO regex validator for all languages.
#         validators=[],
#     )
#
#     # TODO regex validator for all languages.
#     phone = models.CharField(
#         max_length=10,
#         verbose_name='phone',
#         validators=[],
#         help_text='Enter valid phone number',
#     )
#
#     email = models.EmailField(verbose_name='email')
#
#     active = models.BooleanField(default=True)
#     owner = models.CharField(max_length=30)
#     # Attributes - Optional
#     description = models.TextField(blank=True, null=True)
#
#     # Object Manager
#     # Custom Properties Methods
#     # Meta and String
#     class Meta:
#         default_related_name = 'companies'
#         verbose_name = 'company'
#         verbose_name_plural = 'companies'

class RestaurantOwner(models.Model):
    # Relations
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='restaurant_owner'
    )

    gender = models.IntegerField(choices=Gender.choices, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    # email = models.EmailField(verbose_name='email')


class Customer(models.Model):
    # Relations
    user = models.OneToOneField(
        User,
        related_name='customers'
    )
    # company = models.ForeignKey(
    #     Company,
    #     on_delete=models.CASCADE,
    #     related_name='customers'
    # )
    # Attributes - Mandatory
    # worker_id = models.IntegerField(primary_key=True)
    # first_name = models.CharField(
    #     max_length=30,
    #     validators=[name_validator],
    # )
    #
    # last_name = models.CharField(
    #     max_length=30,
    #     validators=[name_validator],
    # )

    # email = models.EmailField(verbose_name='email')
    # Attributes - Optional
    # Object Manager
    # Custom Properties Methods
    # Meta and String


class Order(models.Model):
    # Relations
    restaurant = models.ForeignKey(
        Restaurant,
        related_name='order',
        on_delete=models.CASCADE,
    )
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='orders')
    dishes = models.ManyToManyField(
        Dish,
        related_name='orders',
        verbose_name='dish',
        blank=True,
    )

    # def get_total_price(self):
    #     return self.dishes.aggregate(sum=Sum('price'))['sum']

    # Attributes - Mandatory
    # name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=7)

    # Attributes - Optional
    # description = models.CharField(max_length=100, null=True, blank=True)

    # Object Manager
    # Custom Properties Methods
    # Meta and String

    def __str__(self):
        return "ID:#{} - Restaurant: {} - Dishes: {} - Total: ${}".format(self.id, self.restaurant, self.dishes, self.price)

        # def __init__(self, *args, **kwargs):
        #     # self.price = Dish.objects.filter(restaurant=self.restaurant).aggregate(sum=Sum('price'))['sum']
        #     self.price = 5
        #     logger = logging.getLogger(__name__)
        #     logger.error(kwargs)
        #     super().__init__(*args, **kwargs)

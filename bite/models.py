from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.db import models
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
# TODO move this validator to somewhere else!
name_validator = RegexValidator(r'^[a-zA-Z]+$')


# TODO add imagaField for restaurant image, resize it.
class Restaurant(models.Model):
    # Relations
    # Attributes - Mandatory
    name = models.CharField(
        max_length=30,
        validators=[],
    )
    address = models.CharField(
        max_length=100,
        verbose_name='address',
        help_text='Enter a valid address(City, Street, Number)',
        # TODO regex validator for all languages.
        validators=[],
    )

    # TODO regex validator for all languages.
    phone = models.CharField(
        max_length=10,
        verbose_name='phone',
        validators=[],
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
        return "{}-{}-{}-{}".format(self.name, self.price, self.description, self.restaurant)


class Company(models.Model):
    # Relations
    restaurant = models.ManyToManyField(
        Restaurant,
        related_name='companies',
        verbose_name='restaurant',
        null=True,
        blank=True,
    )
    # Attributes - Mandatory
    name = models.CharField(
        max_length=30,
        validators=[],
    )
    address = models.CharField(
        max_length=100,
        verbose_name='address',
        help_text='Enter valid address(City, Street, Number)',
        # TODO regex validator for all languages.
        validators=[],
    )

    # TODO regex validator for all languages.
    phone = models.CharField(
        max_length=10,
        verbose_name='phone',
        validators=[],
        help_text='Enter valid phone number',
    )

    email = models.EmailField(verbose_name='email')

    active = models.BooleanField(default=True)
    owner = models.CharField(max_length=30)
    # Attributes - Optional
    description = models.TextField(blank=True, null=True)

    # Object Manager
    # Custom Properties Methods
    # Meta and String
    class Meta:
        default_related_name = 'companies'
        verbose_name = 'company'
        verbose_name_plural = 'companies'


class Customer(models.Model):
    # Relations
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='customers'
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='customers'
    )
    # Attributes - Mandatory
    worker_id = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(
        max_length=30,
        validators=[name_validator],
    )

    last_name = models.CharField(
        max_length=30,
        validators=[name_validator],
    )

    email = models.EmailField(verbose_name='email')
    # Attributes - Optional
    # Object Manager
    # Custom Properties Methods
    # Meta and String

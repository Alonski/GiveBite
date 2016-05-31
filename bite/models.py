from django.db import models


# Create your models here.
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
    popularity = models.PositiveIntegerField(default=0, editable=False)

    # Object Manager
    # Custom Properties Methods
    # Meta and String
    class Meta:
        verbose_name = 'restaurant'
        verbose_name_plural = 'restaurants'

    def __str__(self):
        return "{} - {}".format(self.name, self.phone)

class Dish(models.Model):
    # Relations
    restaurant = models.ForeignKey(
        Restaurant,
        related_name='dishes',
        on_delete=models.CASCADE,
    )
    # Attributes - Mandatorgit
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=3)
    # Attributes - Optional
    desc = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    # Object Manager
    # Custom Properties Methods
    # Meta and String

    def __str__(self):
        return "{}-{}-{}".format(self.name, self.price, self.desc)

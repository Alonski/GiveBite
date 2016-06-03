from django.contrib import admin
import logging

from .models import *

# Register your models here.

logger = logging.getLogger(__name__)


class DishInLine(admin.TabularInline):
    model = Dish
    extra = 1


class OrdersInLine(admin.TabularInline):
    model = Order
    extra = 1

    rest = Restaurant
    rest_id = 0

    def get_fieldsets(self, request, obj=None):
        self.rest = obj
        self.rest_id = obj.id
        self.price = 5
        return super().get_fieldsets(request, obj)

    # fk_name = 'restaurant'

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == "dishes":
            # logger.error(self.rest)
            kwargs["queryset"] = Dish.objects.filter(restaurant=self.rest)
        # else:
            # logger.error(db_field)
        return super(OrdersInLine, self).formfield_for_manytomany(db_field, request, **kwargs)

    def get_queryset(self, request):
        logger.error(self.rest)
        logger.error(self.model.objects.all())
        return super().get_queryset(request)


class RestaurantAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     ('Question Text', {'fields': ['question_text']}),
    #     ('Date Info', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    inlines = [DishInLine, OrdersInLine]

    # list_display = ('question_text', 'pub_date', 'was_published_recently')
    # list_filter = ['pub_date']
    # search_fields = ['question_text']


# admin.site.register(models.Company)
# admin.site.register(models.Customer)
# admin.site.register(models.Dish)
admin.site.register(Restaurant, RestaurantAdmin)
# admin.site.register(models.Order)

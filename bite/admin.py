from django.contrib import admin
from . import models


# Register your models here.

class DishInLine(admin.TabularInline):
    model = models.Dish
    extra = 1


class RestaurantAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     ('Question Text', {'fields': ['question_text']}),
    #     ('Date Info', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    inlines = [DishInLine]
    # list_display = ('question_text', 'pub_date', 'was_published_recently')
    # list_filter = ['pub_date']
    # search_fields = ['question_text']


admin.site.register(models.Company)
admin.site.register(models.Customer)
# admin.site.register(models.Dish)
admin.site.register(models.Restaurant, RestaurantAdmin)

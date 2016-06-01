from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.utils.encoding import force_text
from django.views.generic import *
from .models import *
import six

# Create your views here.
from bite.models import Restaurant


class IndexView(ListView):
    template_name = 'bite/index.html'

    # context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return None


class RestaurantListView(ListView):
    page_title = "Restaurants List"
    model = Restaurant


class RestaurantDetailView(DetailView):
    page_title = "Restaurant Detail"
    model = Restaurant


class DishListView(ListView):
    page_title = "Dishes List"
    model = Dish

    def get(self, request, restaurant_id, *args, **kwargs):
        self.restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(restaurant=self.restaurant)


class DishMixin:
    fields = (
        'name',
        'price',
        'description',
        'restaurant',
        'id',
    )
    success_url = reverse_lazy('bite:dishes_list')
    model = Dish

    def get(self, request, restaurant_id, *args, **kwargs):
        self.restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        return super().get(request, *args, **kwargs)


class DishCreateView(DishMixin, CreateView):
    page_title = "Dishes Add"

    def get_success_url(self):
        if 'restaurant_id' in self.kwargs:
            restaurant_id = self.kwargs['restaurant_id']
        else:
            restaurant_id = 'none'
        return reverse('bite:dishes_list', kwargs={'restaurant_id': restaurant_id})


class DishUpdateView(DishMixin, UpdateView):
    page_title = "Dishes Edit"
    button_label = "Update"

    def get_success_url(self):
        if 'restaurant_id' in self.kwargs:
            restaurant_id = self.kwargs['restaurant_id']
        else:
            restaurant_id = 'none'
        return reverse('bite:dishes_list', kwargs={'restaurant_id': restaurant_id})


class DishViewView(DishMixin, FormView):
    page_title = "Dishes View"


class DishDeleteView(DishMixin, DeleteView):
    page_title = "Dishes Delete"
    button_label = "Delete"

    def get_success_url(self):
        if 'restaurant_id' in self.kwargs:
            restaurant_id = self.kwargs['restaurant_id']
        else:
            restaurant_id = 'none'
        return reverse('bite:dishes_list', kwargs={'restaurant_id': restaurant_id})


class RestaurantCreateView(CreateView):
    fields = (
        'name',
        'address',
        'phone',
        'email',
        'active',
        'owner',
        'description',
        'popularity',
    )

    success_url = reverse_lazy('bite:restaurant_list')
    model = Restaurant

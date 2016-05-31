from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import *
from .models import *

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


class ListDishes(ListView):
    page_title = "Dishes List"
    model = Dish

    def get_context_data(self, **kwargs):
        context = super(ListDishes, self).get_context_data(**kwargs)
        context['restaurant_idd'] = context
        return context
    # def get_queryset(self):
    #     return super().get_queryset().all()


class DishMixin:
    fields = (
        'name',
        'price',
        'description',
        'restaurant',
    )
    success_url = reverse_lazy('bite:dishes_list')
    model = Dish


class DishCreateView(DishMixin, CreateView):
    page_title = "Dishes Add"


class DishUpdateView(DishMixin, UpdateView):
    page_title = "Dishes Edit"
    button_label = "Update"


class DishViewView(DishMixin, FormView):
    page_title = "Dishes View"


class DishDeleteView(DishMixin, DeleteView):
    page_title = "Dishes Delete"
    button_label = "Delete"

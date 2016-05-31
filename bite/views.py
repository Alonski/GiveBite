from django.shortcuts import render
from django.views.generic import *
# Create your views here.
from bite.models import Restaurant


class IndexView(ListView):
    template_name = 'bite/index.html'
    # context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return None

class RestaurantListView(ListView):
    model = Restaurant
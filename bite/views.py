from django.shortcuts import render
from django.views.generic import *
# Create your views here.

class IndexView(ListView):
    template_name = 'bite/index.html'
    # context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return None
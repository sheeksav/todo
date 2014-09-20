from django.views.generic import TemplateView, FormView, View
from django.shortcuts import render

from .models import ToDoList, ToDoItem

# Create your views here.

class ToDoListDisplayView(TemplateView):
    template_name = 'engine/home.html'

    def get_context_data(self, **kwargs):

        try:
            tasks = ToDoItem.objects.filter(complete=False)
        except ToDoItem.DoesNotExit:
            tasks = None

        return {
            'tasks': tasks,
        }


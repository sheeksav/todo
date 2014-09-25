from django.views.generic import TemplateView, FormView, View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext

from .models import ToDoList, ToDoItem
from .forms import AddTaskForm

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


class AddTaskFormView(FormView):
    form_class = AddTaskForm
    template_name = 'engine/new_task.html'
    success_url = '/'

    def form_valid(self, form):

        task = ToDoItem.objects.create(
            #list = ToDoList.objects.get(owner=self.request.user),
            list = ToDoList.objects.get(id=1),
            title = form.cleaned_data.get('title'),
            description = form.cleaned_data.get('description'),
        )

        return super(AddTaskFormView, self).form_valid(form)


class CompleteTaskAPIView(View):
    http_method_names = ['post', ]

    def post(self, request, *args, **kwargs):

        task_id = request.POST.get('pk')

        task = ToDoItem.objects.get(id=task_id)
        task.complete = True
        task.save()

        response = {
            'success': True,
        }

        return HttpResponse(response, content_type='application/json')













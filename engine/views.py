from django.views.generic import TemplateView, FormView, View
from django.shortcuts import render, redirect

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
            list = ToDoList.objects.get(owner=self.request.user),
            description = form.cleaned_data.get('description'),
        )

        return super(AddTaskFormView, self).form_valid(form)


def CompleteTaskView(request, pk):

    task = ToDoItem.objects.get(id=pk)
    task.complete = True
    task.save()

    return redirect('home')












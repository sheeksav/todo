from django.views.generic import TemplateView, FormView, View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import UserProfile, ToDoList, ToDoItem
from .forms import AddTaskForm, LoginForm, SignUpForm


# Create your views here.

class SignUpView(FormView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = '/'

    def form_valid(self, form):

        # Get data from form
        email = form.cleaned_data.get('email').lower()
        username = email[:30] # Limit to 30 chars
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        password = form.cleaned_data.get('password')

        # Create a new user object
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)

        # Authenticate the user
        user = authenticate(username=username, password=password)

        # Create user profile
        profile = UserProfile.objects.create(
            user=user,
        )

        # Create a new task list for the user
        list = ToDoList.objects.create(owner=user)

        # Log the user in
        login(self.request, user)

        return super(SignUpView, self).form_valid(form)


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = ''

    def get_context_data(self, **kwargs):

        context = super(LoginView, self).get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next')

        return context

    def form_valid(self, form):

        username = User.objects.get(email=form.cleaned_data.get('email')).username
        user = authenticate(username=username, password=form.cleaned_data.get('password'))

        if user:
            login(self.request, user)

        if 'next' in self.request.GET:
            self.success_url = self.request.GET.get('next')
        else:
            self.success_url = '/tasks/'

        return super(LoginView, self).form_valid(form)


class LogoutView(View):

    def get(self, request):
        logout(request)

        return redirect('home')


class HomeView(TemplateView):
    template_name = 'engine/home.html'


class ToDoListDisplayView(TemplateView):
    template_name = 'engine/tasks.html'

    def get_context_data(self, **kwargs):

        try:
            list = ToDoList.objects.get(owner=self.request.user)
            tasks = ToDoItem.objects.filter(list=list, complete=False)
        except ToDoItem.DoesNotExit:
            tasks = None

        return {
            'tasks': tasks,
        }


class AddTaskFormView(FormView):
    form_class = AddTaskForm
    template_name = 'engine/new_task.html'
    success_url = '/tasks/'

    def form_valid(self, form):

        task = ToDoItem.objects.create(
            list = ToDoList.objects.get(owner=self.request.user),
            #list = ToDoList.objects.get(id=1),
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













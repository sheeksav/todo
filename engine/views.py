from django.views.generic import TemplateView, FormView, View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives

from django.conf import settings


from .models import UserProfile, ToDoList, ToDoItem, BusinessUnit, Goal
from .forms import AddTaskForm, AssignTaskForm, LoginForm, SignUpForm, ActivateForm


# Create your views here.

class SignUpView(FormView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = '/tasks/'

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


class ActivateView(FormView):
    template_name = 'activate.html'
    form_class = ActivateForm
    success_url = '/tasks/'

    def dispatch(self, request, *args, **kwargs):

        token = kwargs.get('token')
        pk = kwargs.get('pk')

        try:
            user = User.objects.get(profile__auth_token=token)
        except User.DoesNotExist:
            return redirect('home')

        kwargs['user'] = user

        return super(ActivateView, self).dispatch(request, *args, **kwargs)


    def form_valid(self, form):

        user = User.objects.get(profile__auth_token=self.kwargs.get('token'))

        user.username = user.email[:30]
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.set_password(form.cleaned_data['password'])
        user.save()

        # Authenticate the user
        user = authenticate(username=user.username, password=form.cleaned_data['password'])

        # Log the user in
        login(self.request, user)

        return super(ActivateView, self).form_valid(form)


class HomeView(TemplateView):
    template_name = 'engine/home.html'


class ToDoListDisplayView(TemplateView):
    template_name = 'engine/tasks.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):

        return super(ToDoListDisplayView, self).dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):

        list = ToDoList.objects.get(owner=self.request.user)

        try:
            tasks = ToDoItem.objects.filter(list=list, complete=False, from_admin=False)
        except ToDoItem.DoesNotExist:
            tasks = None

        try:
            assigned_tasks = ToDoItem.objects.filter(list=list, complete=False, from_admin=True)
        except ToDoItem.DoesNotExist:
            assigned_tasks = None

        return {
            'tasks': tasks,
            'assigned_tasks': assigned_tasks,
        }


class AddTaskFormView(FormView):
    form_class = AddTaskForm
    template_name = 'engine/new_task.html'
    success_url = '/tasks/'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):

        return super(AddTaskFormView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        task = ToDoItem.objects.create(
            list = ToDoList.objects.get(owner=self.request.user),
            title = form.cleaned_data.get('title'),
            description = form.cleaned_data.get('description'),
            creator = self.request.user,
        )

        return super(AddTaskFormView, self).form_valid(form)


class AssignTaskFormView(FormView):
    form_class = AssignTaskForm
    template_name = 'engine/assign_task.html'
    success_url = '/tasks/'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):

        return super(AssignTaskFormView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        try:
            assignee = User.objects.get(email=form.cleaned_data.get('assignee'))
            html_message = '<p>A new task item has been assigned to you. You\'d better <a href="http://'+settings.SITE_URL+'/tasks">go do it now</a>!</p>'
        except User.DoesNotExist:
            assignee = User.objects.create_user(username=form.cleaned_data.get('assignee').lower()[:30], email=form.cleaned_data.get('assignee').lower())
            list = ToDoList.objects.create(owner=assignee)
            profile = UserProfile.objects.create(user=assignee)
            html_message = '<p>A new task item has been assigned to you. You\'d better <a href="http://'+settings.SITE_URL+'/activate/'+assignee.profile.auth_token+'">go do it now</a>!</p>'

        task = ToDoItem.objects.create(
            list = ToDoList.objects.get(owner=assignee.pk),
            title = form.cleaned_data.get('title'),
            from_admin = True,
            description = form.cleaned_data.get('description'),
            creator = self.request.user,
        )

        # Send the email
        subject = u"New ToDo Assigned to You"
        message = u"A new task has been assigned to you. You'd better go do it!"
        html_message = html_message
        sender = self.request.user.email
        recipient = assignee.email

        subject, from_email, to = subject, sender, recipient
        text_content = message
        html_content = html_message
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


        return super(AssignTaskFormView, self).form_valid(form)


# class AssignTaskFormView(TemplateView):
#     template_name = 'engine/assign_task.html'
#     http_method_names = ['get', 'post', ]
#
#     def dispatch(self, request, *args, **kwargs):
#
#         # Here we are somehow buildilng the list of people
#         people = (('', '--------'), )
#         for p in User.objects.all().order_by('last_name'):
#             people = people + ((p.id, p.get_full_name()), )
#
#         self.assignees = people
#
#         return super(AssignTaskFormView, self).dispatch(request, *args, **kwargs)
#
#
#     def get(self, request, *args, **kwargs):
#
#         context = self.get_context_data(**kwargs)
#         context['form'] = AssignTaskForm(assignees=self.assignees)
#
#         return self.render_to_response(context)
#
#
#     def post(self, requets, *args, **kwargs):
#
#         form = AssignTaskForm(assignees=self.assignees)
#
#         if form.is_valid():
#             # Create the task
#
#             if form.cleaned_data.get('assignee', None):
#                 try:
#                     assignee = User.objects.get(pk=form.cleaned_data.get('assignee'))
#                 except (User.DoesNotExist, User.MultipleObjectsReturned):
#                     assignee = None
#             else:
#                 assignee = None
#
#
#             task = ToDoItem.objects.create(
#                 list = ToDoList.objects.get(owner__pk=assignee.user.pk),
#                 title = form.cleaned_data.get('title'),
#                 from_admin = True,
#                 description = form.cleaned_data.get('description'),
#             )
#
#         return redirect('tasks')


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


class AcceptTaskAPIView(View):
    http_method_names = ['post', ]

    def post(self, request, *args, **kwargs):

        task_id = request.POST.get('pk')

        task = ToDoItem.objects.get(id=task_id)
        task.from_admin = False
        task.save()

        response = {
            'sucess': True,
        }

        return HttpResponse(response, content_type='application/json')


class TaskDetailView(TemplateView):
    template_name = 'engine/task-detail.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):

        task_id = kwargs.get('pk')

        try:
            task = ToDoItem.objects.get(pk=task_id)
        except DoesNotExist:
            return redirect('tasks')

        kwargs['task'] = task

        return super(TaskDetailView, self).dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):

        task = ToDoItem.objects.get(pk = kwargs.get('pk'))
        creator = task.creator.get_full_name

        context = {
            'task': task,
            'description': task.description,
            'creator': creator,
        }

        return context


def CompleteTaskView(request, pk):

    if pk:
        t = ToDoItem.objects.get(pk=pk)
        t.complete = True
        t.save()

    return redirect('tasks')


def AcceptTaskView(request, pk):

    if pk:
        t = ToDoItem.objects.get(pk=pk)
        t.from_admin = False
        t.save()

    return redirect('tasks')


def DeleteTaskView(request, pk):

    if pk:
        t = ToDoItem.objects.get(pk=pk)
        t.delete()

    return redirect('tasks')


class DashboardView(TemplateView):
    template_name = 'engine/dashboard.html'

    def get_context_data(self):

        biz_units = BusinessUnit.objects.all()

        context = {
            'biz_units': biz_units,
        }

        return context



class GoalsView(TemplateView):
    template_name = 'engine/biz_unit_goals.html'


    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):

        try:
            unit = BusinessUnit.objects.get(pk=kwargs.get('pk'))
        except BusinessUnit.DoesNotExist:
            return redirect('dashboard')

        try:
            goals = Goal.objects.filter(business_unit=kwargs.get('pk'))
        except Goal.DoesNotExist:
            return redirect('dashboard')

        kwargs['unit'] = unit
        kwargs['goals'] = goals

        return super(GoalsView, self).dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):

        return {
            'unit': kwargs.get('unit'),
            'goals': kwargs.get('goals'),
        }







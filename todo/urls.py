from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from engine.views import HomeView, LoginView, SignUpView, LogoutView, ToDoListDisplayView, CompleteTaskAPIView, \
    AddTaskFormView, AssignTaskFormView, AcceptTaskAPIView, ActivateView, TaskDetailView, CompleteTaskView, \
    AcceptTaskView, DeleteTaskView, DashboardView, GoalsView, GoalsDetailView, AddUnitView, AddGoalView, \
    UpdateTaskStatusView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^tasks/$', ToDoListDisplayView.as_view(), name='tasks'),
    url(r'^new-task/$', AddTaskFormView.as_view(), name='add-task'),
    url(r'^assign-task/(?P<pk>\d+)/', AssignTaskFormView.as_view(), name='assign-task'),
    url(r'^details/(?P<pk>\d+)/$', TaskDetailView.as_view(), name='task-detail'),
    # url(r'^complete-task/(?P<pk>\d+)/$', CompleteTaskAPIView.as_view(), name='complete-task-api'),
    # url(r'^accept-task/(?P<pk>\d+)/$', AcceptTaskAPIView.as_view(), name='accept-task-api'),
    url(r'^complete-task/(?P<pk>\d+)/$', CompleteTaskView, name='complete-task'),
    url(r'^accept-task/(?P<pk>\d+)/$', AcceptTaskView, name='accept-task'),
    url(r'^delete-task/(?P<pk>\d+)/$', DeleteTaskView, name='delete-task'),
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'^dashboard/unit/add/$', AddUnitView.as_view(), name='add-unit'),
    url(r'^dashboard/goals/(?P<pk>\d+)/$', GoalsView.as_view(), name='goals'),
    url(r'^dashboard/goals/add/(?P<pk>\d+)/$', AddGoalView.as_view(), name='goals-add'),
    url(r'^dashboard/goals/tasks/(?P<pk>\d+)/$', GoalsDetailView.as_view(), name='goals-detail'),
    url(r'^task/update/(?P<pk>\d+)/(?P<status>\d+)/$', UpdateTaskStatusView, name='update-status'),


    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^activate/(?P<token>[-\w]+)/$', ActivateView.as_view(), name='activate'),

)

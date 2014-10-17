from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from engine.views import HomeView, LoginView, SignUpView, LogoutView, ToDoListDisplayView, CompleteTaskAPIView, \
    AddTaskFormView, AssignTaskFormView, AcceptTaskAPIView, ActivateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^tasks/$', ToDoListDisplayView.as_view(), name='tasks'),
    url(r'^new-task/$', AddTaskFormView.as_view(), name='add-task'),
    url(r'^assign-task/$', AssignTaskFormView.as_view(), name='assign-task'),
    url(r'^complete-task/(?P<pk>\d+)/$', CompleteTaskAPIView.as_view(), name='complete-task-api'),
    url(r'^accept-task/(?P<pk>\d+)/$', AcceptTaskAPIView.as_view(), name='accept-task-api'),

    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^activate/$', ActivateView.as_view(), name='activate'),

)

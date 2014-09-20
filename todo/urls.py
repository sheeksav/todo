from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from engine.views import ToDoListDisplayView, CompleteTaskView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', ToDoListDisplayView.as_view(), name='home'),
    url(r'^complete/(?P<pk>\d+)/$', CompleteTaskView, name='complete-task'),

)

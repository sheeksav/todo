from django.contrib import admin
from .models import UserProfile, ToDoList, ToDoItem, BusinessUnit, Goal, Resource

admin.site.register(UserProfile)
admin.site.register(ToDoList)
admin.site.register(ToDoItem)
admin.site.register(BusinessUnit)
admin.site.register(Goal)
admin.site.register(Resource)

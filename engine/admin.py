from django.contrib import admin
from .models import UserProfile, ToDoList, ToDoItem, BusinessUnit, Goal

admin.site.register(UserProfile)
admin.site.register(ToDoList)
admin.site.register(ToDoItem)
admin.site.register(BusinessUnit)
admin.site.register(Goal)

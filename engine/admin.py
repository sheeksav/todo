from django.contrib import admin
from .models import UserProfile, ToDoList, ToDoItem

admin.site.register(UserProfile)
admin.site.register(ToDoList)
admin.site.register(ToDoItem)

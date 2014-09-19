from django.db import models
from django.contrib.auth.models import User

class ToDoList(models.Model):
    owner = models.ForeignKey(User)

class ToDoItem(models.Model):
    list = models.ForeignKey(ToDoList)
    description = models.CharField(max_length=300)
    complete = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now_add=True)







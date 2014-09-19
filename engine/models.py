from django.db import models
from django.contrib.auth.models import User

class ToDoList(models.Model):
    owner = models.ForeignKey(User)

    def __str__(self):
        return u'To-Do List for %s' % self.owner.get_full_name()


class ToDoItem(models.Model):
    list = models.ForeignKey(ToDoList)
    description = models.CharField(max_length=300)
    complete = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description









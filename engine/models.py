from django.db import models
from django.contrib.auth.models import User
import string
import random


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    is_admin = models.BooleanField(default=False)

    auth_token = models.TextField(blank=True, default=u'')

    def __unicode__(self):
        return u'Profile for %s' % self.user

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if not self.auth_token:
            self.auth_token = ''.join(random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits
            ) for _ in range(32))

        return super(UserProfile, self).save(force_insert, force_update, using, update_fields)


class ToDoList(models.Model):
    owner = models.ForeignKey(User)

    def __str__(self):
        return u'To-Do List for %s' % self.owner.email


class ToDoItem(models.Model):
    list = models.ForeignKey(ToDoList)
    creator = models.ForeignKey(User)
    title = models.CharField(blank=False, max_length=100)
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    from_admin = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BusinessUnit(models.Model):
    name = models.CharField(max_length=300)
    manager = models.ForeignKey(User, blank=True)

    def __str__(self):
        return self.name

    










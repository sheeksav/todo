from django.db import models
from django.contrib.auth.models import User
import string
import random


PROJECT_STATUS = (
    ('good', 'I\'m in good shape'),
    ('help', 'I need help'),
    ('trouble', 'I am in trouble'),
)


class BaseModel(models.Model):

    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class UserProfile(BaseModel):
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


class ToDoList(BaseModel):
    owner = models.ForeignKey(User)

    def __str__(self):
        return u'To-Do List for %s' % self.owner.email



class BusinessUnit(BaseModel):
    name = models.CharField(max_length=300)
    manager = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return self.name


class Goal(BaseModel):
    name = models.CharField(max_length=300)
    owner = models.ForeignKey(User, null=True, blank=True)
    business_unit = models.ForeignKey(BusinessUnit, related_name='goals')

    def __str__(self):
        return self.name


class ToDoItem(BaseModel):
    list = models.ForeignKey(ToDoList)
    creator = models.ForeignKey(User)
    title = models.CharField(blank=False, max_length=100)
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    from_admin = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now_add=True)
    goal = models.ForeignKey(Goal, related_name='tasks')
    status = models.CharField(max_length=30, choices=PROJECT_STATUS, default='good')

    def __str__(self):
        return self.title


class Resource(BaseModel):
    name = models.CharField(max_length=300)
    link = models.CharField(max_length=300)
    task = models.ForeignKey(ToDoItem)
    creator = models.ForeignKey(User)

    def __str__(self):
        return self.name


class Comment(BaseModel):
    text = models.TextField(max_length=1000)
    author = models.ForeignKey(User)
    task = models.ForeignKey(ToDoItem)

    def __str__(self):
        return u'Comment by %s' % self.author













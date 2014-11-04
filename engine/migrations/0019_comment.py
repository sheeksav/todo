# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('engine', '0018_resource'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('text', models.TextField(max_length=1000)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(to='engine.ToDoItem')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]

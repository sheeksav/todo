# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0016_auto_20141102_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessunit',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='businessunit',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goal',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goal',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todoitem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todoitem',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todolist',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todolist',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
            preserve_default=True,
        ),
    ]

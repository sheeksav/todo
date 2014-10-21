# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('engine', '0006_todoitem_from_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='creator',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]

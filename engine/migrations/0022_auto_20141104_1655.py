# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0021_auto_20141104_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='owner',
            field=models.ForeignKey(related_name=b'goals', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]

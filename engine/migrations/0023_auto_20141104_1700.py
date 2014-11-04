# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0022_auto_20141104_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='business_unit',
            field=models.ForeignKey(related_name=b'goals', to='engine.BusinessUnit'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='owner',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]

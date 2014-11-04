# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0023_auto_20141104_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='goal',
            field=models.ForeignKey(related_name=b'tasks', to='engine.Goal'),
        ),
    ]

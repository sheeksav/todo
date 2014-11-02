# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0012_goal_business_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='goal',
            field=models.ForeignKey(default='', to='engine.Goal'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0015_auto_20141102_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='status',
            field=models.CharField(max_length=30, choices=[(b'1', b"I'm in good shape"), (b'2', b'I need help'), (b'3', b'I am in trouble')]),
        ),
    ]

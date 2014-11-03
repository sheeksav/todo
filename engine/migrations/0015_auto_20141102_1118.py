# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0014_todoitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='status',
            field=models.CharField(max_length=30, choices=[(1, b"I'm in good shape"), (2, b'I need help'), (3, b'I am in trouble')]),
        ),
    ]

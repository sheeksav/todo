# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0013_todoitem_goal'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='status',
            field=models.CharField(default='', max_length=30, choices=[(b'good', b"I'm in good shape"), (b'need_help', b'I need help'), (b'in_trouble', b'I am in trouble')]),
            preserve_default=False,
        ),
    ]

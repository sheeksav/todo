# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0020_auto_20141104_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='status',
            field=models.CharField(default=b'good', max_length=30, choices=[(b'good', b"I'm in good shape"), (b'help', b'I need help'), (b'trouble', b'I am in trouble')]),
        ),
    ]

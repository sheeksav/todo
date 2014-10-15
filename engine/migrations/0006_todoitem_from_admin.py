# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0005_userprofile_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='from_admin',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

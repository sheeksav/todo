# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0011_auto_20141101_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='business_unit',
            field=models.ForeignKey(default='', to='engine.BusinessUnit'),
            preserve_default=False,
        ),
    ]

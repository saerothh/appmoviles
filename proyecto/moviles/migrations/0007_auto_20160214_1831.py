# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviles', '0006_auto_20160214_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movil',
            name='microsd',
            field=models.BooleanField(choices=[(True, 'Si'), (False, 'No')]),
        ),
    ]

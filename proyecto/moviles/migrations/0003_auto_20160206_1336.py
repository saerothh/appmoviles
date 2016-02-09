# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviles', '0002_auto_20160206_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valoracion',
            name='valoracion',
            field=models.PositiveIntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
        ),
    ]

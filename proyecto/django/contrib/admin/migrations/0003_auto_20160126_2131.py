# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0002_logentry_remove_auto_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logentry',
            name='action_time',
            field=models.DateTimeField(auto_now=True, verbose_name='action time'),
        ),
    ]

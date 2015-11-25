# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movil',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('fecha_lanzamiento', models.DateTimeField(default=django.utils.timezone.now)),
                ('fabricante', models.CharField(max_length=200)),
                ('versionOS', models.CharField(max_length=5)),
            ],
        ),
    ]

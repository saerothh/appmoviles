# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviles', '0004_movil_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movil',
            name='image',
            field=models.ImageField(upload_to='moviles', blank=True),
        ),
    ]

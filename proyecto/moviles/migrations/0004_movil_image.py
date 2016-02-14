# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviles', '0003_auto_20160206_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='movil',
            name='image',
            field=models.ImageField(blank=True, upload_to='moviles/static/img'),
        ),
    ]

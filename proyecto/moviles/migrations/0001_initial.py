# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(default='Anonimo', max_length=100)),
                ('texto', models.TextField(help_text='Tu comentario', verbose_name='Comentario')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
            },
        ),
        migrations.CreateModel(
            name='Movil',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(unique=True, max_length=30)),
                ('fecha_lanzamiento', models.DateField(default=django.utils.timezone.now)),
                ('fabricante', models.CharField(max_length=30)),
                ('versionOS', models.CharField(max_length=30)),
                ('tam_pantalla', models.CharField(max_length=4)),
                ('mem_ram', models.CharField(default='--', max_length=10)),
                ('microsd', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Movil',
                'verbose_name_plural': 'Moviles',
            },
        ),
        migrations.CreateModel(
            name='Valoracion',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('valoracion', models.PositiveIntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('movil', models.ForeignKey(to='moviles.Movil')),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Valoracion',
                'verbose_name_plural': 'Valoraciones',
            },
        ),
        migrations.AddField(
            model_name='comentario',
            name='movil',
            field=models.ForeignKey(to='moviles.Movil'),
        ),
    ]

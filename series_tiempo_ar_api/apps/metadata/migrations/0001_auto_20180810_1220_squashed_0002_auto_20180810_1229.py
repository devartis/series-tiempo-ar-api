# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-10 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', 'enhanced_meta_name_change'),
    ]

    operations = [
        migrations.CreateModel(
            name='Synonym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms', models.TextField(help_text='Lista de términos similares, separados por coma, sin espacios ni mayúsculas. Ejemplo "ipc,inflacion"', unique=True)),
            ],
        ),
    ]

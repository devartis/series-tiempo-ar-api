# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-01 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSVDumpTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('RUNNING', 'Procesando catálogos'), ('FINISHED', 'Finalizada')], max_length=20)),
                ('created', models.DateTimeField()),
                ('finished', models.DateTimeField(null=True)),
                ('logs', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

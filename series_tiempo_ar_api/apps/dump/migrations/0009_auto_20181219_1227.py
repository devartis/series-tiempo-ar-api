# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-19 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dump', '0008_auto_20181129_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generatedumptask',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
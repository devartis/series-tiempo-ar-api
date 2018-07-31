# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-25 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('analytics', '0008_auto_20180725_1114'), ('analytics', '0009_query_uri')]

    dependencies = [
        ('analytics', '0007_query_api_mgmt_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='request_time',
            field=models.DecimalField(decimal_places=25, default=0, max_digits=30),
        ),
        migrations.AddField(
            model_name='query',
            name='status_code',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='query',
            name='user_agent',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='query',
            name='uri',
            field=models.TextField(default=''),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-18 23:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amount', '0004_auto_20170713_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spent',
            name='name',
        ),
    ]

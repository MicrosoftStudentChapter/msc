# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-09 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0052_auto_20180809_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secretarie',
            name='post',
            field=models.CharField(choices=[('1st', 'GENERAL SECRETARY'), ('2nd', 'Financial SECRETARY'), ('3rd', 'JOINT SECRETARY')], default='2nd', max_length=50),
        ),
    ]

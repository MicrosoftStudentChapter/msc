# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2018-03-20 22:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0042_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Author',
            new_name='author',
        ),
    ]
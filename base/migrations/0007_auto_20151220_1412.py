# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-20 14:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20151220_1407'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sessionbasket',
            old_name='session_id',
            new_name='session_key',
        ),
    ]

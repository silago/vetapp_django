# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 21:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20151227_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproducts',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Order'),
            preserve_default=False,
        ),
    ]

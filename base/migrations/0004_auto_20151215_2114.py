# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-15 21:14
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_product_creation_ts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-28 17:59
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_auto_20161027_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='original',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='original'),
        ),
    ]

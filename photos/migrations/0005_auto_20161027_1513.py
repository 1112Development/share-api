# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-27 22:13
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20161027_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(max_length=1000, upload_to=''),
        ),
    ]

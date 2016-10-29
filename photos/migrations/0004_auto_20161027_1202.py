# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-27 19:02
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_photo_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='original',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='thumbnail',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='uploaded_at',
        ),
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(max_length=1000, upload_to='', null=True),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-01 21:08
from __future__ import unicode_literals

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CloudinaryImage',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('format', models.CharField(editable=False, max_length=255)),
                ('height', models.CharField(editable=False, max_length=255)),
                ('width', models.CharField(editable=False, max_length=255)),
                ('bytes', models.IntegerField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('lat', models.FloatField(max_length=255)),
                ('long', models.FloatField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('image',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='photos.CloudinaryImage')),
            ],
        ),
    ]

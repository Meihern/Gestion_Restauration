# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-19 20:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181219_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

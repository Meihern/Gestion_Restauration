# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-19 20:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20181219_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='Client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
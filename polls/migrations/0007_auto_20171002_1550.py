# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-02 12:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20171002_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='dept',
            field=models.CharField(blank=True, max_length=35),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='users',
            name='surname',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='users',
            name='usrId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-27 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20171027_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='img',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]

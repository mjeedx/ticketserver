# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-21 10:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_auto_20170421_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='cartridge',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2020-03-02 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SW_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('ipv4', models.CharField(max_length=15)),
                ('mac', models.CharField(max_length=17)),
            ],
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-07-18 13:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('family_name', models.CharField(max_length=20)),
                ('fathers_name', models.CharField(max_length=20)),
                ('tel', models.CharField(max_length=17)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Tel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel_1', models.CharField(max_length=13)),
            ],
        ),
        migrations.AddField(
            model_name='contacts',
            name='department_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Department'),
        ),
        migrations.AddField(
            model_name='contacts',
            name='mail_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Mail'),
        ),
        migrations.AddField(
            model_name='contacts',
            name='position_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Position'),
        ),
    ]

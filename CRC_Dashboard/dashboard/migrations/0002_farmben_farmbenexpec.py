# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-25 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farmben',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flav', models.IntegerField()),
                ('consist', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Farmbenexpec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmerID', models.CharField(max_length=5)),
                ('flavour', models.IntegerField()),
                ('consistency', models.IntegerField()),
            ],
        ),
    ]

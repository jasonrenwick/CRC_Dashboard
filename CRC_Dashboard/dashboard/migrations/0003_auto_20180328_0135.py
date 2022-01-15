# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-28 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_farmben_farmbenexpec'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criteria', models.CharField(max_length=1)),
                ('criteria_weight', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Criterions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criterionID', models.CharField(max_length=3)),
                ('criterion_weight', models.IntegerField()),
                ('criterion_text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Farmerscores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmerID', models.CharField(max_length=4)),
                ('A1', models.IntegerField()),
                ('A2', models.IntegerField()),
                ('A3', models.IntegerField()),
                ('A4', models.IntegerField()),
                ('A5', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Farmben',
        ),
        migrations.DeleteModel(
            name='Farmbenexpec',
        ),
    ]
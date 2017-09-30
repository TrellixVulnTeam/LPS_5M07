# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-23 22:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Letters', '0001_initial'),
        ('Students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Students.Student'),
        ),
    ]

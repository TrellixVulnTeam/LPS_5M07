# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-14 19:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import teacher.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherLetters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letterfile', models.FileField(blank=True, upload_to=teacher.models.user_directory_path)),
                ('date_of_upload', models.DateField(auto_now_add=True)),
                ('description', models.CharField(default=' ', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

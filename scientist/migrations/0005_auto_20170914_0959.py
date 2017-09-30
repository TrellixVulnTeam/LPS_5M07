# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-14 16:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scientist', '0004_studentinfo_userletters_userstudentinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userletters',
            name='letterfile',
            field=models.FileField(blank=True, upload_to='letters/'),
        ),
        migrations.AlterField(
            model_name='userletters',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usermailingaddress',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userstudentinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

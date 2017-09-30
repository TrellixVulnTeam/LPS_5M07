# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-24 19:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Letters', '0002_letter_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='from_scientist',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='letter',
            name='from_student',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='letter',
            name='received_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='letter',
            name='sent_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='letter',
            name='letterfile',
            field=models.FileField(blank=True, upload_to='letters/'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='scientist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Scientist', to=settings.AUTH_USER_MODEL),
        ),
    ]

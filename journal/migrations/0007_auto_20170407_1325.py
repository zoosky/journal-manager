# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 13:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0006_auto_20170407_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalmember',
            name='journal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='journal.Journal'),
        ),
    ]
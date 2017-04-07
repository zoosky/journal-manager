# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 10:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0004_journal_modified'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('version', models.PositiveSmallIntegerField(default=1)),
                ('pubkey', models.BinaryField()),
                ('content', models.BinaryField()),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
    ]

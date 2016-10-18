# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 17:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_wallets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='members',
            field=models.ManyToManyField(related_name='my_wallets', through='wallet.Balance', to=settings.AUTH_USER_MODEL),
        ),
    ]

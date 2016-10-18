# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 00:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_wallet_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balance',
            name='balance',
        ),
        migrations.AddField(
            model_name='balance',
            name='member_balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='members',
            field=models.ManyToManyField(related_name='wallet_members', through='wallet.Balance', to=settings.AUTH_USER_MODEL),
        ),
    ]
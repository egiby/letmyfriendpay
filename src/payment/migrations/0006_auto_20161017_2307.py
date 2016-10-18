# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 23:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_auto_20161017_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='members',
            field=models.ManyToManyField(related_name='payment_members', through='payment.Transaction', to=settings.AUTH_USER_MODEL),
        ),
    ]
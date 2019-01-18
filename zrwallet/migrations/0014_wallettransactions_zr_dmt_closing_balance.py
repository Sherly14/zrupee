# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-16 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zrwallet', '0013_wallet_dmt_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallettransactions',
            name='zr_dmt_closing_balance',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=10),
        ),
    ]

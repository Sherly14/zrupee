# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-07-18 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zrcommission', '0028_commission_is_settled'),
    ]

    operations = [
        migrations.AddField(
            model_name='dmtcommissionstructure',
            name='sender_fee_limit',
            field=models.DecimalField(decimal_places=4, default=None, max_digits=7, null=True),
        ),
    ]

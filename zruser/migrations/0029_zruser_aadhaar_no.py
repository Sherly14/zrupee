# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-29 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zruser', '0028_merge_20180227_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='zruser',
            name='aadhaar_no',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]

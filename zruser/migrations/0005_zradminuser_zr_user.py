# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-06 04:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zruser', '0004_merchantlead'),
    ]

    operations = [
        migrations.AddField(
            model_name='zradminuser',
            name='zr_user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='zr_user', to='zruser.ZrUser'),
        ),
    ]

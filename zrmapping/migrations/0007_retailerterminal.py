# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-13 13:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zruser', '0027_zrterminal'),
        ('zrmapping', '0006_auto_20170923_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='RetailerTerminal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('at_created', models.DateTimeField(auto_now_add=True)),
                ('at_modified', models.DateTimeField(auto_now=True)),
                ('is_attached_to_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('retailer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='terminal_retailer_mappings', to='zruser.ZrUser')),
                ('terminal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retailer_terminal_mappings', to='zruser.ZrTerminal')),
            ],
            options={
                'verbose_name_plural': 'RetailerTerminalMappings',
            },
        ),
    ]

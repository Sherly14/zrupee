# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-03-23 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zrcommission', '0032_auto_20190323_2209'),
        ('zrmapping', '0008_aepscommission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aepscommission',
            name='aeps_commission_structure_set',
        ),
        migrations.AddField(
            model_name='aepscommission',
            name='aeps_commission_structure',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aeps_comm_mappings', to='zrcommission.AEPSCommissionStructure'),
        ),
        migrations.AlterField(
            model_name='aepscommission',
            name='distributor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dist_aeps_comm_mappings', to='zruser.ZrUser'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 20:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zrtransaction', '0002_auto_20170625_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCircle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('at_created', models.DateTimeField(auto_now_add=True)),
                ('at_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=512)),
                ('code', models.CharField(max_length=256)),
                ('is_enabled', models.BooleanField(default=True)),
                ('transaction_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zrtransaction.TransactionType')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zrtransaction.Vendor')),
            ],
            options={
                'verbose_name_plural': 'ServiceCircles',
            },
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('at_created', models.DateTimeField(auto_now_add=True)),
                ('at_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=512)),
                ('code', models.CharField(max_length=256)),
                ('min_amount', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('max_amount', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('is_enabled', models.BooleanField(default=True)),
                ('transaction_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zrtransaction.TransactionType')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zrtransaction.Vendor')),
            ],
            options={
                'verbose_name_plural': 'ServiceProviders',
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-23 17:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_type', models.CharField(max_length=20, verbose_name='信用类型')),
                ('credit_desc', models.CharField(max_length=100, verbose_name='信用类型描述')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '信用类型',
                'verbose_name_plural': '信用类型',
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-11 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0004_auto_20170511_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='name',
            field=models.CharField(blank=True, help_text='Name for box to differ boxes with same plant', max_length=30, null=True),
        ),
    ]

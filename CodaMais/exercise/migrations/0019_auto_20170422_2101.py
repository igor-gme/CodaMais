# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-23 00:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0018_auto_20170422_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userexercise',
            name='number_submission',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-30 18:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0006_submission_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 30, 18, 40, 1, 134023, tzinfo=utc)),
        ),
    ]

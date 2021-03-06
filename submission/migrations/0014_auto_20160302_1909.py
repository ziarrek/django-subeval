# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-02 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import submission.models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0013_auto_20160302_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='command',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='submission',
            name='package',
            field=models.FileField(upload_to=submission.models.submission_directory_path),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-02 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0012_auto_20160302_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='package',
            field=models.FileField(upload_to=b'submissions'),
        ),
    ]
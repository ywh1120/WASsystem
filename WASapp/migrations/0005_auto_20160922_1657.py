# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-22 07:57
from __future__ import unicode_literals

import WASapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WASapp', '0004_auto_20160922_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfdata',
            name='pdffile',
            field=models.FileField(null='true', upload_to=WASapp.models.generate_filename),
        ),
    ]
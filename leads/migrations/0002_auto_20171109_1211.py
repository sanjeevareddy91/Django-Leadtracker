# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-09 06:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='joinings',
            old_name='Status',
            new_name='status',
        ),
    ]

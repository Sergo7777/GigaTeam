# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 19:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20170220_1902'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_answer',
            new_name='UserAnswer',
        ),
    ]

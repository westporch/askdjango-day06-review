# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 06:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['id']},
        ),
    ]
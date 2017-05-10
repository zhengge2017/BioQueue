# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-10 01:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0003_auto_20170505_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='type',
            field=models.SmallIntegerField(choices=[(1, 'Disk'), (2, 'Memory'), (3, 'CPU'), (4, 'Virtual Memory')]),
        ),
    ]
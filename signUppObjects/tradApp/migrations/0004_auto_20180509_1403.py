# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-09 14:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tradApp', '0003_auto_20180509_1257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='order_status',
            new_name='status',
        ),
    ]

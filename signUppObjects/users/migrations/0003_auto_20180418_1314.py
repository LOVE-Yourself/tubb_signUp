# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-18 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_coach_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='birday',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='coach_name',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nick_name',
            field=models.CharField(blank=True, default='拓吧叭学员', max_length=50, null=True, verbose_name='昵称'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-09 11:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True, verbose_name='昵称')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='年龄')),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], max_length=5)),
                ('address', models.CharField(max_length=100, verbose_name='区域')),
                ('telphone', models.CharField(blank=True, max_length=11, null=True)),
                ('catgory', models.CharField(choices=[('c1', '高级'), ('c2', '中级'), ('c3', '低级')], default='c1', max_length=10, verbose_name='驾驶证类型')),
                ('students', models.IntegerField(default=0, verbose_name='学生人数')),
                ('years_old', models.IntegerField(default=0, verbose_name='驾龄')),
                ('long_td', models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True, verbose_name='经度')),
                ('lati_td', models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True, verbose_name='纬度')),
                ('code', models.CharField(blank=True, max_length=20, null=True, verbose_name='城市编码')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '教练信息',
                'verbose_name_plural': '教练信息',
            },
        ),
        migrations.CreateModel(
            name='CoachActiveAdress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True, verbose_name='名称')),
                ('address', models.CharField(max_length=100, verbose_name='区域')),
                ('long_td', models.DecimalField(decimal_places=7, max_digits=10, verbose_name='经度')),
                ('lati_td', models.DecimalField(decimal_places=7, max_digits=10, verbose_name='纬度')),
                ('code', models.CharField(max_length=20, verbose_name='城市编码')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '教练练习场地',
                'verbose_name_plural': '教练练习场地',
            },
        ),
        migrations.CreateModel(
            name='DriverSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='驾校名称')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '驾校机构',
                'verbose_name_plural': '驾校机构',
            },
        ),
        migrations.AddField(
            model_name='coach',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driverSchool.DriverSchool', verbose_name='所属驾校'),
        ),
    ]

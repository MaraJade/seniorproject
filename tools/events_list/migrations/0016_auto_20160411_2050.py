# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events_list', '0015_auto_20160411_2024'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('urlkey', models.CharField(max_length=50)),
                ('meetupID', models.BigIntegerField(unique=True, verbose_name=b'Meetups.com ID')),
            ],
        ),
        migrations.AlterField(
            model_name='host',
            name='topics',
            field=models.ManyToManyField(related_name='hosts', to='events_list.HostTopic'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events_list', '0017_auto_20160414_0152'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='lastVisit',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

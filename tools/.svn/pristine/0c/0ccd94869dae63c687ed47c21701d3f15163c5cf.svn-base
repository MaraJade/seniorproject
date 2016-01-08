# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('event_url', models.URLField()),
                ('meetupID', models.CharField(unique=True, max_length=50, verbose_name=b'Meetups.com ID')),
                ('description', models.TextField()),
                ('local_start', models.DateTimeField()),
                ('local_end', models.DateTimeField()),
                ('utc_offset', models.BigIntegerField()),
                ('is_applicable', models.BooleanField(default=True, help_text=b'Indicates if an event is applicable to our audience or not.')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=30)),
                ('meetupID', models.BigIntegerField(unique=True, verbose_name=b'Meetups.com ID')),
                ('is_applicable', models.BooleanField(default=True, help_text=b'Indicates if a group is applicable to our audience or not. If marked as not applicable meetups organized by this group will be automatically set to not applicable')),
            ],
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=200)),
                ('datetime', models.DateTimeField(default=datetime.datetime.now)),
                ('action_type', models.CharField(max_length=2, choices=[(b'EU', b'Event Update'), (b'EI', b'Event Import'), (b'GU', b'Group Update')])),
                ('object_id', models.BigIntegerField(null=True, blank=True)),
            ],
            options={
                'ordering': ('-datetime',),
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('bio', models.TextField()),
                ('country', models.CharField(max_length=2)),
                ('state', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=30)),
                ('latitude', models.DecimalField(max_digits=10, decimal_places=6)),
                ('longitude', models.DecimalField(max_digits=10, decimal_places=6)),
                ('url', models.URLField()),
                ('largePhoto', models.URLField()),
                ('photo', models.URLField()),
                ('thumbnail', models.URLField()),
                ('lastVisit', models.DateTimeField()),
                ('meetupID', models.BigIntegerField(unique=True, verbose_name=b'Meetups.com ID')),
                ('groups', models.ManyToManyField(related_name='members', to='events_list.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('urlkey', models.CharField(max_length=50)),
                ('meetupID', models.BigIntegerField(unique=True, verbose_name=b'Meetups.com ID')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='topics',
            field=models.ManyToManyField(related_name='people', to='events_list.Topic'),
        ),
        migrations.AddField(
            model_name='event',
            name='group',
            field=models.ForeignKey(to='events_list.Group'),
        ),
        migrations.AddField(
            model_name='event',
            name='hashtags',
            field=models.ManyToManyField(related_name='events', to='events_list.Hashtag'),
        ),
    ]

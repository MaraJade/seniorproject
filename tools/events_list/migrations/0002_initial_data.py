# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def initial_hashtags(apps, schema_editor):
    Hashtag = apps.get_model("events_list", "Hashtag")
    hashtag = Hashtag(name = "Apache")
    hashtag.save()

class Migration(migrations.Migration):

    dependencies = [
        ('events_list', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_hashtags),
    ]

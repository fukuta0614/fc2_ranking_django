# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.CharField(max_length=120, serialize=False, primary_key=True)),
                ('url', models.CharField(default=b'unknown', max_length=120)),
                ('title', models.CharField(default=b'notitle', max_length=120)),
                ('link', models.CharField(default=b'nolink', max_length=120)),
                ('ginfo_url', models.CharField(default=b'unknown', max_length=120)),
                ('playtime', models.CharField(default=b'unknown', max_length=120)),
                ('thumbnail', models.CharField(default=b'unknown', max_length=120)),
                ('fav', models.IntegerField()),
                ('playing', models.IntegerField()),
            ],
        ),
    ]

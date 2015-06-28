# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20150628_0732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag', models.CharField(max_length=120, serialize=False, primary_key=True)),
                ('num', models.IntegerField()),
            ],
        ),
    ]

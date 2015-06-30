# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_movie_is_adult'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='is_adult',
            field=models.IntegerField(default=1),
        ),
    ]

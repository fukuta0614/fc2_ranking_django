# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import movies.models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='tag',
            field=movies.models.ListField(default=[]),
        ),
    ]

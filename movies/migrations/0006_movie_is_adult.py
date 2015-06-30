# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='is_adult',
            field=models.IntegerField(default=1),
        ),
    ]

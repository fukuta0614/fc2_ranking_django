# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20150628_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='ginfo_url',
            field=models.CharField(default=b'', max_length=120),
        ),
        migrations.AlterField(
            model_name='movie',
            name='link',
            field=models.CharField(default=b'', max_length=120),
        ),
        migrations.AlterField(
            model_name='movie',
            name='play_time',
            field=models.CharField(default=b'', max_length=120),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tag',
            field=models.CharField(default=[], max_length=120),
        ),
        migrations.AlterField(
            model_name='movie',
            name='thumbnail',
            field=models.CharField(default=b'', max_length=120),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(default=b'', max_length=120),
        ),
        migrations.AlterField(
            model_name='movie',
            name='url',
            field=models.CharField(default=b'', max_length=120),
        ),
    ]

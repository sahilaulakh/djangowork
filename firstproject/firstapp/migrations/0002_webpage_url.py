# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='url',
            field=models.URLField(unique=True, default=datetime.datetime(2018, 8, 27, 21, 51, 35, 402960, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

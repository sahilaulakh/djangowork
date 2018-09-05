# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webpage',
            old_name='topic',
            new_name='topics',
        ),
    ]

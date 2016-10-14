# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0006_auto_20161006_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='draft',
            field=models.BooleanField(default=datetime.datetime(2016, 10, 6, 9, 33, 58, 453670, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userpost',
            name='publish',
            field=models.DateField(default=datetime.datetime(2016, 10, 6, 9, 35, 9, 613558, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import newsletter.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsletter', '0005_auto_20161005_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='image',
            field=models.ImageField(height_field=b'height_field', width_field=b'width_field', null=True, upload_to=newsletter.models.upload_location, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_userpost'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userpost',
            options={'ordering': ['-timestamp', '-updated']},
        ),
        migrations.AddField(
            model_name='userpost',
            name='image',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]

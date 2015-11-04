# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_device_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='token_gcm',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
    ]

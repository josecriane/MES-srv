# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_command_devices'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='token',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
    ]

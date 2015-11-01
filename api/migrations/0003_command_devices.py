# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_command'),
    ]

    operations = [
        migrations.AddField(
            model_name='command',
            name='devices',
            field=models.ManyToManyField(related_name='commands', to='api.Device'),
        ),
    ]

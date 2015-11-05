# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20151104_0038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='token_gcm',
            new_name='tokenGCM',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20151109_1806'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='owner_id',
            new_name='owner',
        ),
    ]

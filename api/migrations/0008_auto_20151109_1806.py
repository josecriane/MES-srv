# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20151105_0156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='owner',
            new_name='owner_id',
        ),
    ]

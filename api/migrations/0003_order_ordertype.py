# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_order_ordertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ordertype',
            field=models.ForeignKey(related_name='orders', default=1, to='api.OrderType'),
            preserve_default=False,
        ),
    ]

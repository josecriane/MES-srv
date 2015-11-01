# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('launched', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=40)),
                ('params', models.CharField(default=b'', max_length=255, blank=True)),
                ('owner', models.ForeignKey(related_name='commands', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('launched',),
            },
        ),
    ]

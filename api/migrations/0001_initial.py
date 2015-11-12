# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(default=b'', max_length=13, blank=True)),
                ('uid', models.CharField(max_length=15)),
                ('configured', models.BooleanField(default=False)),
                ('token', models.CharField(default=b'', max_length=255, blank=True)),
                ('tokenGCM', models.CharField(default=b'', max_length=255, blank=True)),
                ('owner', models.ForeignKey(related_name='devices', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='DeviceOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_done', models.BooleanField(default=False)),
                ('device', models.ForeignKey(to='api.Device')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('launched', models.DateTimeField(auto_now_add=True)),
                ('params', models.CharField(default=b'', max_length=255, blank=True)),
            ],
            options={
                'ordering': ('launched',),
            },
        ),
        migrations.CreateModel(
            name='OrderType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(default=b'', max_length=255, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='ordertype',
            field=models.ForeignKey(related_name='orders', to='api.OrderType'),
        ),
        migrations.AddField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deviceorder',
            name='order',
            field=models.ForeignKey(to='api.Order'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-25 09:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0012_auto_20180309_0755'),
    ]

    operations = [
        migrations.CreateModel(
            name='Export',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('export_type', models.CharField(choices=[(b'M', 'Model export'), (b'V', 'Video export')], db_index=True, max_length=1)),
                ('url', models.TextField(default='')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent')),
            ],
        ),
    ]

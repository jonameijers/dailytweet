# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-12-25 00:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_content', models.TextField()),
                ('tweet_content2', models.TextField()),
                ('tweet_content3', models.TextField()),
            ],
        ),
    ]

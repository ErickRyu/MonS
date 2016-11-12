# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-18 18:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ac_book', '0009_auto_20161018_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_ConCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ac_book.ConsumeCategory')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

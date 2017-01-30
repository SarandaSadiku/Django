# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-28 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_and_registration_app', '0002_auto_20170128_1333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='pw_hash',
            new_name='password',
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=200),
        ),
    ]

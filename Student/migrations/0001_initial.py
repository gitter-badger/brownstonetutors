# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20150506_1210'),
        ('Client', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.IntegerField()),
                ('client', models.ForeignKey(to='Client.Client')),
                ('profile', models.OneToOneField(related_name='student_profile', verbose_name='profile', to='account.Profile')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easymoney


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '__first__'),
        ('Tutor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='invoice',
            field=models.ForeignKey(default=0, to='Client.Invoice'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutorstudentrelationship',
            name='client_rate',
            field=easymoney.MoneyField(default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='tutorstudentrelationship',
            name='tutor_rate',
            field=easymoney.MoneyField(default=0, max_digits=12),
        ),
    ]

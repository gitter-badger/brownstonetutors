# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tutor', '0002_auto_20150506_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='invoice',
            field=models.ForeignKey(blank=True, to='Client.Invoice', null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='status',
            field=models.CharField(default=b'SCHEDULED', max_length=30, choices=[(b'SCHEDULED', b'Scheduled'), (b'CANCELLED_ON_TIME', b'Cancelled on time'), (b'CANCELLED_LATE', b'Cancelled late'), (b'CONFIRMED', b'Confirmed'), (b'APPROVED', b'Approved')]),
        ),
    ]

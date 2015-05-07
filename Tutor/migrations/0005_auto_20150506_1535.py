# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tutor', '0004_auto_20150506_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='invoice',
            field=models.ForeignKey(default=1, to='Client.Invoice'),
            preserve_default=False,
        ),
    ]

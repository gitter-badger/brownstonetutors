# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Subjects', '0001_initial'),
        ('Tutor', '0007_auto_20150506_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='tutorstudentsubjectrate',
            name='subjects',
        ),
        migrations.AddField(
            model_name='tutorstudentsubjectrate',
            name='subjects',
            field=models.ForeignKey(default=1, to='Subjects.Subject'),
            preserve_default=False,
        ),
    ]

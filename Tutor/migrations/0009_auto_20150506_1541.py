# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tutor', '0008_auto_20150506_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='invoice',
            field=models.ForeignKey(blank=True, to='Client.Invoice', null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='tutor_student_rel_sub',
            field=models.ForeignKey(default=1, to='Tutor.TutorStudentSubjectRate'),
            preserve_default=False,
        ),
    ]

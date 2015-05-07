# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tutor', '0005_auto_20150506_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='tutor_student_rel_sub',
            field=models.ForeignKey(default=1, to='Tutor.TutorStudentSubjectRate'),
            preserve_default=False,
        ),
    ]

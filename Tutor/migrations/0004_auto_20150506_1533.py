# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easymoney


class Migration(migrations.Migration):

    dependencies = [
        ('Subjects', '0001_initial'),
        ('Tutor', '0003_auto_20150506_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='TutorStudentSubjectRate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tutor_rate', easymoney.MoneyField(default=0, max_digits=12)),
                ('client_rate', easymoney.MoneyField(default=0, max_digits=12)),
                ('subjects', models.ManyToManyField(to='Subjects.Subject')),
            ],
        ),
        migrations.RemoveField(
            model_name='session',
            name='tutor_student_rel',
        ),
        migrations.RemoveField(
            model_name='tutorstudentrelationship',
            name='client_rate',
        ),
        migrations.RemoveField(
            model_name='tutorstudentrelationship',
            name='subjects',
        ),
        migrations.RemoveField(
            model_name='tutorstudentrelationship',
            name='tutor_rate',
        ),
        migrations.AddField(
            model_name='tutorstudentsubjectrate',
            name='tutor_student_rel',
            field=models.ForeignKey(to='Tutor.TutorStudentRelationship'),
        ),
        migrations.AddField(
            model_name='session',
            name='tutor_student_rel_sub',
            field=models.ForeignKey(blank=True, to='Tutor.TutorStudentSubjectRate', null=True),
        ),
    ]

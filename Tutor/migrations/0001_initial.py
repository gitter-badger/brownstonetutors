# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import easymoney


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20150506_1210'),
        ('Subjects', '0001_initial'),
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='time_to_occur')),
                ('status', models.CharField(max_length=30, choices=[(b'SCHEDULED', b'Scheduled'), (b'CANCELLED_ON_TIME', b'Cancelled on time'), (b'CANCELLED_LATE', b'Cancelled late'), (b'CONFIRMED', b'Confirmed'), (b'APPROVED', b'Approved')])),
                ('subject', models.ForeignKey(to='Subjects.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('balance_owed', easymoney.MoneyField(default=0, max_digits=12)),
                ('profile', models.OneToOneField(related_name='tutor_profile', verbose_name='profile', to='account.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='TutorStudentRelationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student', models.ForeignKey(to='Student.Student')),
                ('subjects', models.ManyToManyField(to='Subjects.Subject')),
                ('tutor', models.ForeignKey(to='Tutor.Tutor')),
            ],
        ),
        migrations.AddField(
            model_name='tutor',
            name='students',
            field=models.ManyToManyField(to='Student.Student', through='Tutor.TutorStudentRelationship'),
        ),
        migrations.AddField(
            model_name='session',
            name='tutor_student_rel',
            field=models.ForeignKey(to='Tutor.TutorStudentRelationship'),
        ),
    ]

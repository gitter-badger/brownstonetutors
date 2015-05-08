from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from allauth.account.models import Profile
from Subjects.models import Subject
from Student.models import Student
from Calendar.models import Session, SESSION_STATE_DESCRIPTIONS

from easymoney import MoneyField

class Tutor(models.Model):
	profile = models.OneToOneField(Profile, 
								unique=True, 
								verbose_name=_('profile'), 
								related_name='tutor_profile')
	balance_owed = MoneyField(default=0)
	students = models.ManyToManyField(Student, through='TutorStudentRelationship')

	def __unicode__(self):
		return unicode(self.profile)

class TutorStudentRelationship(models.Model):
	tutor = models.ForeignKey(Tutor)
	student = models.ForeignKey(Student)

	def __unicode__(self):
		return unicode(self.tutor) + " tutoring " + unicode(self.student)

class TutorStudentSubjectRate(models.Model):
	tutor_student_rel = models.ForeignKey(TutorStudentRelationship)
	subjects = models.ForeignKey(Subject)

	tutor_rate = MoneyField(default=0)
	client_rate = MoneyField(default=0)

	def __unicode__(self):
		return unicode(self.tutor_student_rel) + " in " + unicode(self.subjects)

class SessionStatePayModifiers(models.Model):
	session_state = models.CharField(max_length=30, choices = SESSION_STATE_DESCRIPTIONS)
	pay_percentage = models.IntegerField(default=0)

	def __unicode__(self):
		return unicode(self.session_state)

class SessionPay(models.Model):
	session = models.ForeignKey(Session)
	tutor_pay = MoneyField(default=0)

	def __unicode__(self):
		return unicode(self.session)

	"""
	def calculate_client_charge(self):
		charge = self.session.tutor_student_rel_sub.client_rate
		if(session.state == 'cance')
	"""
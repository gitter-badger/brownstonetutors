from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from allauth.account.models import Profile
from Student.models import Student
from Subjects.models import Subject
from Client.models import Invoice

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

class Session(models.Model):
	STATUSES = (
		('SCHEDULED', 'Scheduled'),
		('CANCELLED_ON_TIME', 'Cancelled on time'),
		('CANCELLED_LATE', 'Cancelled late'),
		('CONFIRMED', 'Confirmed'),
		('APPROVED', 'Approved'),
	)

	invoice = models.ForeignKey(Invoice, blank=True, null=True)

	tutor_student_rel_sub = models.ForeignKey(TutorStudentSubjectRate)
	time = models.DateTimeField(verbose_name=_('time_to_occur'),
								   default=timezone.now)
	status = models.CharField(max_length=30, choices=STATUSES, default='SCHEDULED')

	def save(self, force_insert=False, force_update=False):
		our_client = self.tutor_student_rel_sub.tutor_student_rel.student.client
		our_invoice = Invoice.objects.filter(client=our_client).filter(
			month=self.time.month).filter(
			year=self.time.year)
		if our_invoice.count() > 0:
			our_invoice = our_invoice[0]
		else:
			our_invoice = Invoice.objects.create(client=our_client,
									month=self.time.month,
									year=self.time.year)
		self.invoice = our_invoice
		super(Session, self).save(force_insert, force_update)

	def get_client_rate(self):
		return self.tutor_student_rel_sub.client_rate

	def get_tutor_rate(self):
		return self.tutor_student_rel_sub.tutor_rate

	def __unicode__(self):
		return unicode(self.tutor_student_rel_sub.tutor_student_rel) + " at " + unicode(self.time)
from django.db import models
from django.utils.translation import ugettext_lazy as _

from allauth.account.models import Profile, Address
from Client.models import Client

class Student(models.Model):
	profile = models.OneToOneField(Profile, 
                                unique=True, 
                                verbose_name=_('profile'), 
                                related_name='student_profile')
	client = models.ForeignKey(Client)
	grade = models.IntegerField()

	def __unicode__(self):
		return unicode(self.profile)
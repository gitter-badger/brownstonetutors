from django.db import models
from django.utils.translation import ugettext_lazy as _

from allauth.account.models import Profile, Address

from easymoney import MoneyField

class Client(models.Model):
	profile = models.OneToOneField(Profile, 
								unique=True, 
								verbose_name=_('profile'), 
								related_name='client_profile')
	outstanding_balance = MoneyField(default=0)

	def __unicode__(self):
		return unicode(self.profile)

class Invoice(models.Model):
	MONTH_CHOICES = (
		(1,"January"), 
		(2,"February"), 
		(3, 'March'),
		(4, 'April'),
		(5, 'May'),
		(6, 'June'),
		(7, 'July'),
		(8, 'August'),
		(9, 'September'),
		(10, 'October'),
		(11, 'November'),
		(12, 'December'))

	year = models.IntegerField()
	month = models.IntegerField(choices=MONTH_CHOICES)
	client = models.ForeignKey(Client)

	def __unicode__(self):
		return unicode(self.client) + ": " + unicode(self.month) + "/" + unicode(self.year)
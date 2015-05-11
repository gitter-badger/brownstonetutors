from django.db import models
from django.conf import settings

from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from django_fsm import FSMKeyField, transition

from Client.models import Invoice, SessionBill

class SessionState(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    label = models.CharField(max_length=63)

    def __unicode__(self):
        return self.label


class Session(models.Model):
    tutor_student_rel_sub = models.ForeignKey('Tutor.TutorStudentSubjectRate')
    time = models.DateTimeField(verbose_name=_('time_to_occur'),
                                   default=timezone.now)
    session_state = FSMKeyField(SessionState, default='scheduled')

    def can_confirm(self):
        return timezone.now > self.time

    @transition(field=session_state, source='scheduled', target='unconfirmed', 
            conditions=[can_confirm])
    def session_time_passed(self):
        return self.can_confirm()

    @transition(field=session_state, source='unconfirmed', target='confirmed')
    def confirm(self):
            client = self.tutor_student_rel_sub.tutor_student_rel.student.client
            invoice = Invoice.objects.filter(client=client).filter(
                month=self.time.month).filter(
                year=self.time.year)
            if invoice.count() > 0:
                invoice = invoice[0]
            else:
                invoice = Invoice.objects.create(client=our_client,
                                        month=self.time.month,
                                        year=self.time.year)
            #Client.models

    def get_client_rate(self):
        return self.tutor_student_rel_sub.client_rate

    def get_tutor_rate(self):
        return self.tutor_student_rel_sub.tutor_rate

    def __unicode__(self):
        return unicode(self.tutor_student_rel_sub.tutor_student_rel) + " at " + unicode(self.time)
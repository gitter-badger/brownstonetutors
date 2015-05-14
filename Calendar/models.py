from django.db import models
from django.conf import settings

from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from django_fsm import FSMKeyField, transition

from Client.models import Invoice, SessionBill

from schedule.models import Event

class SessionState(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    label = models.CharField(max_length=63)

    def __unicode__(self):
        return unicode(self.label)


class SessionEvent(Event):
    tutor_student_rel_sub = models.ForeignKey('Tutor.TutorStudentSubjectRate')
    session_state = FSMKeyField(SessionState, default='scheduled')

    def can_confirm(self):
        return timezone.now > self.start

    @transition(field=session_state, source='scheduled', target='unconfirmed', 
            conditions=[can_confirm])
    def session_time_passed(self):
        return self.can_confirm()

    @transition(field=session_state, source='unconfirmed', target='confirmed')
    def confirm(self):
            client = self.tutor_student_rel_sub.tutor_student_rel.student.client
            invoice = Invoice.objects.filter(client=client).filter(
                month=self.start.month).filter(
                year=self.start.year)
            if invoice.count() > 0:
                invoice = invoice[0]
            else:
                invoice = Invoice.objects.create(client=our_client,
                                        month=self.start.month,
                                        year=self.start.year)
            #Client.models

    def get_client_rate(self):
        return self.tutor_student_rel_sub.client_rate

    def get_tutor_rate(self):
        return self.tutor_student_rel_sub.tutor_rate

    def __unicode__(self):
        return unicode(self.tutor_student_rel_sub.tutor_student_rel) + " at " + unicode(self.start)
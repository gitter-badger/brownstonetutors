from django.db import models

from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from django_states.fields import StateField
from django_states.machine import StateMachine, StateDefinition, StateTransition, StateGroup
from django_states.models import StateModel

SESSION_STATE_DESCRIPTIONS = (
    ('scheduled' , _('Session scheduled')),
    ('unconfirmed' , _('Session uncomfirmed')),
    ('confirmed' , _('Session comfirmed')),
    ('cancelled_late' , _('Session cancelled late')),
    ('cancelled_last_minute' , _('Session cancelled last minute')),
    ('no_show' , _('Student no show')),
)

class SessionStateMachine(StateMachine):
    log_transitions = True

    class scheduled(StateDefinition):
        description = SESSION_STATE_DESCRIPTIONS[0]
        initial = True

    class unconfirmed(StateDefinition):
        description = SESSION_STATE_DESCRIPTIONS[1]

    class confirmed(StateDefinition):
        description = SESSION_STATE_DESCRIPTIONS[2]

    class cancelled_late(StateDefinition):
        description = SESSION_STATE_DESCRIPTIONS[3]

    class cancelled_last_minute(StateDefinition):
        description = SESSION_STATE_DESCRIPTIONS[4]

    class no_show(StateDefinition):
        description = SESSION_STATE_DESCRIPTIONS[5]

    class cancelled(StateGroup):
        states = ['cancelled_late', 
                    'cancelled_last_minute', 'no_show']

    class client_charged(StateGroup):
        states = ['confirmed', 'cancelled_late', 
                    'cancelled_last_minute', 'no_show']

class Session(StateModel):
    tutor_student_rel_sub = models.ForeignKey('Tutor.TutorStudentSubjectRate')
    time = models.DateTimeField(verbose_name=_('time_to_occur'),
                                   default=timezone.now)
    session_state = StateField(machine=SessionStateMachine, default='scheduled')

    """
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
    """

    def get_client_rate(self):
        return self.tutor_student_rel_sub.client_rate

    def get_tutor_rate(self):
        return self.tutor_student_rel_sub.tutor_rate

    def __unicode__(self):
        return unicode(self.tutor_student_rel_sub.tutor_student_rel) + " at " + unicode(self.time)
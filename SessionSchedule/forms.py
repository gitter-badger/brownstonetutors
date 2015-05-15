from six.moves.builtins import object
from django import forms
from django.utils.translation import ugettext_lazy as _
from schedule.models import Event, Occurrence
from schedule.forms import EventForm
from models import SessionEvent

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class SessionEventForm(EventForm):
    def __init__(self, *args, **kwargs):
        super(SessionEventForm, self).__init__(*args, **kwargs)

    class Meta(object):
        model = SessionEvent
        exclude = ('creator', 'created_on', 'calendar', 'session_state')
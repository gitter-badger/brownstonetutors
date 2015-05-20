from six.moves.builtins import object
from django import forms
from django.utils.translation import ugettext_lazy as _
from schedule.models import Event, Occurrence
from schedule.forms import EventForm
from models import SessionEvent

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from Tutor.models import TutorStudentSubjectRate, TutorStudentRelationship, Tutor

class SessionEventForm(EventForm):

	def __init__(self, *args, **kwargs):
		self.session = kwargs.get('instance', None)
		self.user = kwargs.pop('user', None)
		self.tutor_student_rel = TutorStudentRelationship.objects.filter(
				tutor = self.session.tutor_student_rel_sub.tutor_student_rel.tutor)
		super(SessionEventForm, self).__init__(*args, **kwargs)
		self.fields['tutor_student_rel_sub'].queryset = TutorStudentSubjectRate.objects.filter(
												tutor_student_rel=self.tutor_student_rel)

	class Meta(object):
		model = SessionEvent
		exclude = ('creator', 'created_on', 'calendar')#, 'session_state')#, 'tutor_student_rel_sub')
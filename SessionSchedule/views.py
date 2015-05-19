from future import standard_library
standard_library.install_aliases()
import json
import pytz
import datetime
from urllib.parse import quote

from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.edit import DeleteView

from schedule.conf.settings import GET_EVENTS_FUNC, OCCURRENCE_CANCEL_REDIRECT
from schedule.forms import EventForm, OccurrenceForm
from schedule.models import Calendar, Occurrence, Event
from schedule.periods import weekday_names
from schedule.utils import check_event_permissions, coerce_date_dict
from utils import check_calendar_permissions
from schedule import views as s_views

from forms import SessionEventForm
from models import SessionEvent

@check_calendar_permissions
def calendar(request, calendar_slug, template='schedule/calendar.html'):
    return s_views.calendar(request, calendar_slug, template)

@check_calendar_permissions
def calendar_by_periods(request, calendar_slug, periods=None, template_name="schedule/calendar_by_period.html"):
    return s_views.calendar_by_periods(request, calendar_slug, periods, template_name)

def session(request, event_id, template_name="session.html"):
    """
    This view is for showing an event. It is important to remember that an
    event is not an occurrence.  Events define a set of reccurring occurrences.
    If you would like to display an occurrence (a single instance of a
    recurring event) use occurrence.
    Context Variables:
    event
        This is the event designated by the event_id
    back_url
        this is the url that referred to this view.
    """
    session_event = get_object_or_404(SessionEvent, id=event_id)

    if not isinstance(session_event, SessionEvent):
        return s_views.event(request, event_id)

    return render(request, template_name, {
        "event": session_event,
        "back_url": None,
    })

@check_event_permissions
def create_or_edit_session(request, calendar_slug, event_id=None, next=None, template_name='create_session.html', form_class=SessionEventForm):
    """
    This function, if it receives a GET request or if given an invalid form in a
    POST request it will generate the following response
    Template:
        schedule/create_event.html
    Context Variables:
    form:
        an instance of EventForm
    calendar:
        a Calendar with id=calendar_id
    if this function gets a GET request with ``year``, ``month``, ``day``,
    ``hour``, ``minute``, and ``second`` it will auto fill the form, with
    the date specifed in the GET being the start and 30 minutes from that
    being the end.
    If this form receives an event_id it will edit the event with that id, if it
    recieves a calendar_id and it is creating a new event it will add that event
    to the calendar with the id calendar_id
    If it is given a valid form in a POST request it will redirect with one of
    three options, in this order
    # Try to find a 'next' GET variable
    # If the key word argument redirect is set
    # Lastly redirect to the event detail of the recently create event
    """

    date = coerce_date_dict(request.GET)
    initial_data = None
    if date:
        try:
            start = datetime.datetime(**date)
            initial_data = {
                "start": start,
                "end": start + datetime.timedelta(minutes=30)
            }
        except TypeError:
            raise Http404
        except ValueError:
            raise Http404

    instance = None
    if event_id is not None:
        try:
            instance = get_object_or_404(SessionEvent, id=event_id)
        except Http404:
            return s_views.create_or_edit_event(request, calendar_slug, event_id, next)

    calendar = get_object_or_404(Calendar, slug=calendar_slug)

    form = form_class(data=request.POST or None, instance=instance, initial=initial_data, user=request.user)

    if form.is_valid():
        event = form.save(commit=False)
        if instance is None:
            event.creator = request.user
            event.calendar = calendar
        event.save()
        next = next or reverse('event', args=[event.id])
        next = s_views.get_next_url(request, next)
        return HttpResponseRedirect(next)

    next = s_views.get_next_url(request, next)
    return render_to_response(template_name, {
        "form": form,
        "calendar": calendar,
        "next": next
    }, context_instance=RequestContext(request))

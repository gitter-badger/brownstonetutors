try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url
from django.views.generic.list import ListView
from schedule.models import Calendar
from schedule.feeds import UpcomingEventsFeed
from schedule.feeds import CalendarICalendar
from schedule.periods import Year, Month, Week, Day
from schedule.views import DeleteEventView
urlpatterns = patterns(
    '',
    # Session Urls
    url(r'^session/create/(?P<calendar_slug>[-\w]+)/$',
        'SessionSchedule.views.create_or_edit_session',
        name='calendar_create_event'),
    url(r'^session/edit/(?P<calendar_slug>[-\w]+)/(?P<event_id>\d+)/$',
        'SessionSchedule.views.create_or_edit_session',
        name='edit_event'),
    url(r'^session/(?P<event_id>\d+)/$',
        'SessionSchedule.views.session',
        name="event"),
    url(r'^session/delete/(?P<event_id>\d+)/$',
        DeleteEventView.as_view(),
        name="delete_event"),
)
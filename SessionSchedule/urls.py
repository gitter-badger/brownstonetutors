try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url
from django.views.generic.list import ListView
from schedule.views import DeleteEventView

urlpatterns = patterns(
    '',
    url(r'^session/create/(?P<calendar_slug>[-\w]+)/$',
        'SessionSchedule.views.create_or_edit_session',
        name='calendar_create_session'),
    url(r'^session/edit/(?P<calendar_slug>[-\w]+)/(?P<event_id>\d+)/$',
        'SessionSchedule.views.create_or_edit_session',
        name='edit_session'),
    url(r'^session/(?P<event_id>\d+)/$',
        'SessionSchedule.views.session',
        name="session"),
    url(r'^session/delete/(?P<event_id>\d+)/$',
        DeleteEventView.as_view(),
        name="delete_session"),
    )
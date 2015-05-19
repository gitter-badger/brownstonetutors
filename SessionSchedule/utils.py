
from six.moves.builtins import object
from functools import wraps
import pytz
import heapq
from annoying.functions import get_object_or_None
from django.http import HttpResponseRedirect
from django.conf import settings
from django.utils import timezone
from django.utils.module_loading import import_string
from schedule.conf.settings import CHECK_EVENT_PERM_FUNC, CHECK_CALENDAR_PERM_FUNC

def check_calendar_permissions(function):
    @wraps(function)
    def decorator(request, *args, **kwargs):
        from schedule.models import Event, Calendar
        user = request.user
        # check event permission
        event = get_object_or_None(Event, pk=kwargs.get('event_id', None))
        # check calendar permissions
        calendar = None
        if event:
            calendar = event.calendar
        elif 'calendar_slug' in kwargs:
            calendar = Calendar.objects.get(slug=kwargs['calendar_slug'])
        allowed = CHECK_CALENDAR_PERM_FUNC(calendar, user)
        if not allowed:
            return HttpResponseRedirect(settings.LOGIN_URL)

        # all checks passed
        return function(request, *args, **kwargs)

    return decorator
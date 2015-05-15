from django.contrib import admin
from models import (
	SessionEvent,
	SessionState)

admin.site.register(SessionEvent)
admin.site.register(SessionState)
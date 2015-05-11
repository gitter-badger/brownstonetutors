from django.contrib import admin
from models import (
	Session,
	SessionState)

admin.site.register(Session)
admin.site.register(SessionState)
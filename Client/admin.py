from django.contrib import admin

from models import Client, Invoice
from Tutor.models import Session

class SessionInline(admin.TabularInline):
	model = Session
	extra = 0

	readonly_fields = ('admin_get_client_rate',)

	def admin_get_client_rate(self, obj):
		return obj.tutor_student_rel_sub.client_rate

class InvoiceAdmin(admin.ModelAdmin):
	inlines = (SessionInline,)

admin.site.register(Client)
admin.site.register(Invoice, InvoiceAdmin)
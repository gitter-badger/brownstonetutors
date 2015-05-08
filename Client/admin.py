from django.contrib import admin

from models import Client, Invoice, SessionBill, SessionStateChargeModifiers

class SessionBillInline(admin.TabularInline):
	model = SessionBill
	extra = 0

	readonly_fields = ('admin_get_client_rate',)

	def admin_get_client_rate(self, obj):
		return obj.session.tutor_student_rel_sub.client_rate

class InvoiceAdmin(admin.ModelAdmin):
	inlines = (SessionBillInline,)

class SessionStateChargeModifiersAdmin(admin.ModelAdmin):
	readonly_fields = ('session_state',)
	def has_add_permission(self, request, obj=None):
		return False
	def has_delete_permission(self, request, obj=None):
		return False

admin.site.register(Client)
admin.site.register(SessionBill)
admin.site.register(SessionStateChargeModifiers, SessionStateChargeModifiersAdmin)
admin.site.register(Invoice, InvoiceAdmin)
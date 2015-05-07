import django
from django.contrib import admin

from .models import EmailConfirmation, EmailAddress, Profile, PhoneNumber, Address
from .adapter import get_adapter

from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from postal.forms import PostalAddressForm

class AddressInline(admin.StackedInline):
	model = Address
	extra = 0

class PhoneNumberInline(admin.TabularInline):
	model = PhoneNumber
	extra = 0
    
class ProfileAdmin(admin.ModelAdmin):
    #list_display = ('user')
    model = Profile
    inlines = (PhoneNumberInline, AddressInline)
    
class EmailAddressAdmin(admin.ModelAdmin):
    list_display = ('email', 'user', 'primary', 'verified')
    list_filter = ('primary', 'verified')
    search_fields = []
    raw_id_fields = ('user',)

    def __init__(self, *args, **kwargs):
        super(EmailAddressAdmin, self).__init__(*args, **kwargs)
        if not self.search_fields and django.VERSION[:2] < (1, 7):
            self.search_fields = self.get_search_fields(None)

    def get_search_fields(self, request):
        base_fields = get_adapter().get_user_search_fields()
        return ['email'] + list(map(lambda a: 'user__' + a, base_fields))


class EmailConfirmationAdmin(admin.ModelAdmin):
    list_display = ('email_address', 'created', 'sent', 'key')
    list_filter = ('sent',)
    raw_id_fields = ('email_address',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(EmailConfirmation, EmailConfirmationAdmin)
admin.site.register(EmailAddress, EmailAddressAdmin)

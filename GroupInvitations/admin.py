from django.contrib import admin

from .models import GroupInvitation
from .forms import InviteModelForm

class GroupInvitationAdmin(admin.ModelAdmin):
    list_display = ('group', 'email', 'sent', 'accepted')
    form = InviteModelForm

    def get_form(self, request, obj=None, **kwargs):
         form = super(GroupInvitationAdmin, self).get_form(request, **kwargs)
         form.user = request.user
         form.request = request
         return form

admin.site.register(GroupInvitation, GroupInvitationAdmin)
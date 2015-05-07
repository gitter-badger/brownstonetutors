from django.contrib import admin

from .models import GroupInvitation


class GroupInvitationAdmin(admin.ModelAdmin):
    list_display = ('group', 'email', 'sent', 'accepted')
    model = GroupInvitation

admin.site.register(GroupInvitation, GroupInvitationAdmin)
from django import forms
from django.utils.translation import ugettext_lazy as _

from allauth.account.forms import AddEmailForm
from .models import GroupInvitation

from django.contrib.auth.models import Group

class InviteForm(AddEmailForm):

    group = forms.ModelChoiceField(
        queryset = Group.objects.all(),
        empty_label=None
    )

    def clean_email(self):
        value = super(InviteForm, self).clean_email()

        errors = {
            "already_invited": _("This e-mail address has already been"
                                 " invited."),
        }

        if GroupInvitation.objects.filter(email__iexact=value,
                                     accepted=False):
            raise forms.ValidationError(errors["already_invited"])

        return value

    def save(self, email, group):
        return GroupInvitation.create(email=email, group=group)

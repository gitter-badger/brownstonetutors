from django import forms
from django.utils.translation import ugettext_lazy as _

from allauth.account.forms import AddEmailForm
from .models import GroupInvitation

from allauth.account.adapter import get_adapter
from allauth.account.models import EmailAddress
from allauth.account import app_settings

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

class InviteModelForm(forms.ModelForm):
    model = GroupInvitation
    email = forms.EmailField(label=_("E-mail"),
                             required=True,
                             widget=forms.TextInput(attrs={"type": "email",
                                                           "size": "30"}))

    class Meta:
        model = GroupInvitation
        fields = ('group', 'email',)

    """def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(InviteModelForm, self).__init__(*args, **kwargs)
    """

    def clean_email(self):
        value = self.cleaned_data["email"]
        value = get_adapter().clean_email(value)
        errors = {
            "this_account": _("This e-mail address is already associated"
                              " with this account."),
            "different_account": _("This e-mail address is already associated"
                                   " with another account."),
        }
        emails = EmailAddress.objects.filter(email__iexact=value)
        if app_settings.UNIQUE_EMAIL:
            if emails.exists():
                raise forms.ValidationError(errors["different_account"])

        errors = {
            "already_invited": _("This e-mail address has already been"
                                 " invited."),
        }

        if GroupInvitation.objects.filter(email__iexact=value,
                                     accepted=False):
            raise forms.ValidationError(errors["already_invited"])

        return value

    def form_valid(self, form):
        group = form.cleaned_data["group"]
        email = form.cleaned_data["email"]

        try:
            invite = form.save(email, group)
            invite.send_invitation(self.request)
        except Exception as e:
            return self.form_invalid(form)
        self.save()
        return super(InviteModelForm, self).form_valid(form)
    
    

    def save(self, *args, **kwargs):
        cleaned_data = super(InviteModelForm, self).clean()
        group = cleaned_data.get("group")
        email = cleaned_data.get("email")
        invite = GroupInvitation.create(email=email, group=group)
        invite.send_invitation(self.request)
        self.instance = invite
        super(InviteModelForm, self).save(*args, **kwargs)
        return invite
    


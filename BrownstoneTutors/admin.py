from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django import forms
from .forms import NewUserCreationForm

admin.site.unregister(User)

class NewUserAdmin(UserAdmin):
	add_form = NewUserCreationForm
	add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')}
        ),
    )

admin.site.register(User, NewUserAdmin)
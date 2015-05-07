from __future__ import unicode_literals

import datetime

from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from django.db import transaction
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.sites.models import Site
from django.utils.encoding import python_2_unicode_compatible
from django.utils.crypto import get_random_string

from ..utils import build_absolute_uri
from .. import app_settings as allauth_app_settings
from . import app_settings
from . import signals

from .utils import user_email
from .managers import EmailAddressManager, EmailConfirmationManager
from .adapter import get_adapter

from phonenumber_field.modelfields import PhoneNumberField
#from djmoney.models.fields import MoneyField
from easy_thumbnails.fields import ThumbnailerImageField
from timezone_field import TimeZoneField

import settings as accounts_settings
from utils import get_gravatar, generate_sha1, get_protocol, get_datetime_now
from django_countries import data as country_data
country_list = [('', '-'*45)] + country_data.COUNTRIES.items()

from django.db.models.signals import post_save
from django.dispatch import receiver

def upload_to_mugshot(instance, filename):
    """
    Uploads a mugshot for a user to the ``USERENA_MUGSHOT_PATH`` and saving it
    under unique hash for the image. This is for privacy reasons so others
    can't just browse through the mugshot directory.
    """
    extension = filename.split('.')[-1].lower()
    salt, hash = generate_sha1(instance.id)
    path = accounts_settings.MUGSHOT_PATH % {'username': instance.user.username,
                                                    'id': instance.user.id,
                                                    'date': instance.user.date_joined,
                                                    'date_now': get_datetime_now().date()}
    return '%(path)s%(hash)s.%(extension)s' % {'path': path,
                                               'hash': hash[:10],
                                               'extension': extension}

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        prof = Profile.objects.filter(first_name = instance.first_name)
        prof = prof.filter(last_name = instance.last_name)
        prof = prof.filter(user__isnull = True)
        if prof.count() == 0:
            Profile.objects.create(user=instance, 
                first_name = instance.first_name,
                last_name = instance.last_name)
        else:
            prof.update(user = instance)

post_save.connect(create_user_profile, sender=User)

class Profile(models.Model):
    MUGSHOT_SETTINGS = {'size': (accounts_settings.MUGSHOT_SIZE,
                        accounts_settings.MUGSHOT_SIZE),
                        'crop': accounts_settings.MUGSHOT_CROP_TYPE}

    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    user = models.OneToOneField(User, 
                                unique=True, 
                                verbose_name=_('user'), 
                                related_name='base_profile',
                                blank = True,
                                null = True)
    timezone = TimeZoneField(default='America/New_York')
    last_active = models.DateTimeField(_('last active'),
                                       blank=True,
                                       null=True,
                                       help_text=_('The last date that the user was active.'))
    mugshot = ThumbnailerImageField(_('mugshot'),
                                    blank=True,
                                    upload_to=upload_to_mugshot,
                                    resize_source=MUGSHOT_SETTINGS,
                                    help_text=_('A personal image displayed in your profile.'))

    def get_mugshot_url(self):
    # First check for a mugshot and if any return that.
        if self.mugshot:
            return self.mugshot.url

        # Use Gravatar if the user wants to.
        if accounts_settings.MUGSHOT_GRAVATAR:
            return get_gravatar(self.user.email,
                                accounts_settings.MUGSHOT_SIZE,
                                accounts_settings.MUGSHOT_DEFAULT)

        # Gravatar not used, check for a default image.
        else:
            if accounts_settings.MUGSHOT_DEFAULT not in ['404', 'mm',
                                                                'identicon',
                                                                'monsterid',
                                                                'wavatar']:
                return accounts_settings.MUGSHOT_DEFAULT
            else:
                return None
    def has_user(self):
        if self.user is not None:
            return True
        else:
            return False

    def __unicode__(self):
        return self.first_name + " " + self.last_name
        """
        if self.user.get_full_name():
            return self.user.get_full_name()
        else:
            return unicode(self.user)
        """

class PhoneNumber(models.Model):
    NUM_TYPES = (
        ('CELL', 'Cell'),
        ('WORK', 'Work'),
        ('FAX', 'Fax'),
        ('HOME', 'Home'),
    )

    profile = models.ForeignKey(Profile)
    phone_number = PhoneNumberField()
    phone_type = models.CharField(max_length=4, choices=NUM_TYPES)

class Address(models.Model):
    profile = models.ForeignKey(Profile, unique=True)

    line1 = models.CharField(max_length=100)
    line2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    country = models.CharField(choices=country_list, max_length=100)

    class Meta:
        verbose_name_plural = 'Addresses'

@python_2_unicode_compatible        
class EmailAddress(models.Model):

    user = models.ForeignKey(allauth_app_settings.USER_MODEL,
                             verbose_name=_('user'))
    email = models.EmailField(unique=app_settings.UNIQUE_EMAIL,
                              verbose_name=_('e-mail address'))
    verified = models.BooleanField(verbose_name=_('verified'), default=False)
    primary = models.BooleanField(verbose_name=_('primary'), default=False)

    objects = EmailAddressManager()

    class Meta:
        verbose_name = _("email address")
        verbose_name_plural = _("email addresses")
        if not app_settings.UNIQUE_EMAIL:
            unique_together = [("user", "email")]

    def __str__(self):
        return "%s (%s)" % (self.email, self.user)

    def set_as_primary(self, conditional=False):
        old_primary = EmailAddress.objects.get_primary(self.user)
        if old_primary:
            if conditional:
                return False
            old_primary.primary = False
            old_primary.save()
        self.primary = True
        self.save()
        user_email(self.user, self.email)
        self.user.save()
        return True

    def send_confirmation(self, request, signup=False):
        confirmation = EmailConfirmation.create(self)
        confirmation.send(request, signup=signup)
        return confirmation

    def change(self, request, new_email, confirm=True):
        """
        Given a new email address, change self and re-confirm.
        """
        with transaction.commit_on_success():
            user_email(self.user, new_email)
            self.user.save()
            self.email = new_email
            self.verified = False
            self.save()
            if confirm:
                self.send_confirmation(request)


@python_2_unicode_compatible
class EmailConfirmation(models.Model):

    email_address = models.ForeignKey(EmailAddress,
                                      verbose_name=_('e-mail address'))
    created = models.DateTimeField(verbose_name=_('created'),
                                   default=timezone.now)
    sent = models.DateTimeField(verbose_name=_('sent'), null=True)
    key = models.CharField(verbose_name=_('key'), max_length=64, unique=True)

    objects = EmailConfirmationManager()

    class Meta:
        verbose_name = _("email confirmation")
        verbose_name_plural = _("email confirmations")

    def __str__(self):
        return "confirmation for %s" % self.email_address

    @classmethod
    def create(cls, email_address):
        key = get_random_string(64).lower()
        return cls._default_manager.create(email_address=email_address,
                                           key=key)

    def key_expired(self):
        expiration_date = self.sent \
            + datetime.timedelta(days=app_settings
                                 .EMAIL_CONFIRMATION_EXPIRE_DAYS)
        return expiration_date <= timezone.now()
    key_expired.boolean = True

    def confirm(self, request):
        if not self.key_expired() and not self.email_address.verified:
            email_address = self.email_address
            get_adapter().confirm_email(request, email_address)
            signals.email_confirmed.send(sender=self.__class__,
                                         request=request,
                                         email_address=email_address)
            return email_address

    def send(self, request, signup=False, **kwargs):
        current_site = kwargs["site"] if "site" in kwargs \
            else Site.objects.get_current()
        activate_url = reverse("account_confirm_email", args=[self.key])
        activate_url = build_absolute_uri(request,
                                          activate_url,
                                          protocol=app_settings.DEFAULT_HTTP_PROTOCOL)
        ctx = {
            "user": self.email_address.user,
            "activate_url": activate_url,
            "current_site": current_site,
            "key": self.key,
        }
        if signup:
            email_template = 'account/email/email_confirmation_signup'
        else:
            email_template = 'account/email/email_confirmation'
        get_adapter().send_mail(email_template,
                                self.email_address.email,
                                ctx)
        self.sent = timezone.now()
        self.save()
        signals.email_confirmation_sent.send(sender=self.__class__,
                                             confirmation=self)

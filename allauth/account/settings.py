from django.conf import settings
gettext = lambda s: s

DEFAULT_USE_HTTPS = False
_USE_HTTPS = getattr(settings, 'USERENA_USE_HTTPS', DEFAULT_USE_HTTPS)

MUGSHOT_GRAVATAR = getattr(settings,
                                   'MUGSHOT_GRAVATAR',
                                   True)

MUGSHOT_GRAVATAR_SECURE = getattr(settings,
                                          'MUGSHOT_GRAVATAR_SECURE',
                                          _USE_HTTPS)

MUGSHOT_DEFAULT = getattr(settings,
                                  'MUGSHOT_DEFAULT',
                                  'identicon')

MUGSHOT_SIZE = getattr(settings,
                               'MUGSHOT_SIZE',
                               80)

MUGSHOT_CROP_TYPE = getattr(settings,
                                    'MUGSHOT_CROP_TYPE',
                                    'smart')

MUGSHOT_PATH = getattr(settings,
                               'MUGSHOT_PATH',
                               'mugshots/')

LANGUAGE_FIELD = getattr(settings,
                                 'LANGUAGE_FIELD',
                                 'language')
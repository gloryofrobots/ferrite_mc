# Django settings for fmc project.
sadasd
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('gloryofrobots', 'gloryofrobots@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mwfcompo_fmc', # Or path to database file if using sqlite3.
        'USER': 'mwfcompo_fmc', # Not used with sqlite3.
        'PASSWORD': '97A9SxOI130', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
#ALLOWED_HOSTS = ['.mwfcomponent.com']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Kiev'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html

ugettext = lambda s: s

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', ugettext('English')),
    ('ru', ugettext('Russian')),
)

SITE_ID = 1

PREFIX_DEFAULT_LOCALE = False
LOCALEURL_USE_ACCEPT_LANGUAGE = True

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

from os.path import abspath, dirname
ROOT_PATH = abspath(dirname(__file__))
APP_ROOT_PATH = abspath(dirname(ROOT_PATH))

#MEDIA_ROOT = APP_ROOT_PATH + '/media/'
MEDIA_ROOT = '/home/mwfcompo/domains/mwfcomponent.com/public_html/media/'
MEDIA_URL = '/media/'

#STATIC_ROOT = APP_ROOT_PATH + '/static/'
STATIC_ROOT = '/home/mwfcompo/domains/mwfcomponent.com/public_html/static/'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/media/'

LOCALE_PATHS = (
    APP_ROOT_PATH + '/locale/',
)

TINYMCE_JS_URL = STATIC_URL + '/tiny_mce/tiny_mce.js'
TINYMCE_JS_ROOT = STATIC_ROOT + '/tiny_mce/'

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "safari,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template",
    'theme_advanced_buttons1': "save,newdocument,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,formatselect,fontselect,fontsizeselect",
    'theme_advanced_buttons2': "cut,copy,paste,pastetext,pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,help,code",
    'theme_advanced_buttons3': "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,iespell,media,advhr,|,print,|,fullscreen",
    'theme_advanced_buttons4': "moveforward,movebackward,absolute,|,styleprops,|,cite,abbr,acronym,del,ins,attribs,|,visualchars,nonbreaking,template,pagebreak,|,insertdate,inserttime,preview,|,forecolor,backcolor",
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_statusbar_location': "bottom",
    'theme_advanced_resizing': True,
    'relative_urls': False,
    'convert_urls': False,
    'width': 600,
    'height' : 200,
}

# Additional locations of static files
STATICFILES_DIRS = (
    APP_ROOT_PATH+"/tinymce/js",
    #"/home/gloryofrobots/develop/django_projects/fmc/tinymce/js",
    #"/home/gloryofrobots/develop/django_projects/fmc/content/static"
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '2ayui@9rue1ndu_)@y#bs-x*tib6$d81(@fjh2$)@(dgo0cu^('

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (

    'content.middleware.ForceDefaultLanguageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'localeurl.middleware.LocaleURLMiddleware',


    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.i18n',
    'django.contrib.auth.context_processors.auth',
    "mothertongue.context_processors.router",
)

ROOT_URLCONF = 'fmc.urls'

# Python dotted path to the WSGI application used by Django's runserver.
#WSGI_APPLICATION = 'fmc.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'filebrowser',
    'tinymce',
    'grappelli',
    'django.contrib.admin',
    'localeurl',
    'mothertongue',
    'content',
    'products',
)



# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


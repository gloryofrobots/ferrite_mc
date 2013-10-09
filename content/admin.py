__author__ = 'gloryofrobots'
# import stuff we need from django
from django.contrib import admin
from django.conf import settings
from django.db import models
# import stuff we need from django
from django.contrib import admin
from django.conf import settings
from tinymce.widgets import TinyMCE
# import app specific shit
from content.models import FrontPage, FrontPageTranslation


class FrontPageTranslationInline(admin.StackedInline):
    model = FrontPageTranslation
    extra = 1
    max_num = len(settings.LANGUAGES)-1
    fieldsets = (
        (None, {
            'fields': ['language',]
        }),
        ('Translation', {
            'fields': ['title','content','description','keywords'],
            'classes': ['collapse',],
        }),
    )
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE},
    }

# create the admin model
class FrontPageAdmin(admin.ModelAdmin):
    fields = ['title','content','description','keywords','alias','menuindex','parent','ispublished','isfolder',]
    inlines = (FrontPageTranslationInline,)

# register with CMS
admin.site.register(FrontPage, FrontPageAdmin)

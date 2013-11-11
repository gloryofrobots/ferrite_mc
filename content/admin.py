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
from content.models import FrontPage, FrontPageTranslation,Chunk,ChunkTranslation


class FrontPageTranslationInline(admin.StackedInline):
    model = FrontPageTranslation
    extra = 1
    max_num = len(settings.LANGUAGES)-1

    inline_classes = ('grp-collapse grp-open',)

    fieldsets = (
        (None, {
            'fields': ['language',]
        }),
        ('Translation', {
            'fields': ['title','content','description','keywords']
        }),
    )
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE},
    }

# create the admin model
class FrontPageAdmin(admin.ModelAdmin):
    fields = ['title','content','description','keywords','alias','menuindex','parent','ispublished','isfolder','inmenu']
    inlines = (FrontPageTranslationInline,)



class ChunkTranslationInline(admin.StackedInline):
    model = ChunkTranslation
    extra = 1
    max_num = len(settings.LANGUAGES)-1

    inline_classes = ('grp-collapse grp-open',)

    fieldsets = (
        (None, {
            'fields': ['language',]
        }),
        ('Translation', {
            'fields': ['content']
        }),
    )



# create the admin model
class ChunkAdmin(admin.ModelAdmin):
    fields = ['name','content']
    inlines = (ChunkTranslationInline,)

# register with CMS
admin.site.register(FrontPage, FrontPageAdmin)
admin.site.register(Chunk, ChunkAdmin)
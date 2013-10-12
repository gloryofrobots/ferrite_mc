from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


from mothertongue.models import MothertongueModelTranslate

from tinymce import models as tinymce_models


class FrontPage(MothertongueModelTranslate):
    title = models.CharField(_('title'), max_length=200, help_text=_('Page title'))
    content = tinymce_models.HTMLField(_('content'), blank=True, help_text=_('Page content'))
    keywords = models.CharField(_('keywords'), max_length=255, help_text=_('Page keywords'))
    description = models.CharField(_('description'), max_length=255, help_text=_('Page description'))

    alias = models.CharField(_('alias'), max_length=200, help_text=_('Page Url Alias'))
    isfolder = models.BooleanField(help_text=_('Is this page a folder'), default=False)

    menuindex = models.PositiveSmallIntegerField(default=0)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL, default=None)

    ispublished = models.BooleanField(help_text=_('Is this page published'), default=True)
    inmenu = models.BooleanField(help_text=_('Is this shows in menu'), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    translations = models.ManyToManyField('FrontPageTranslation', blank=True, verbose_name=_('translations'))
    translation_set = 'frontpagetranslation_set'
    translated_fields = ['title', 'content', 'keywords', 'description']

    def __unicode__(self):
        return u'%s' % self.title

# chunks translations model
class FrontPageTranslation(models.Model):
    front_page_instance = models.ForeignKey('FrontPage', verbose_name=_('front_page'))
    language = models.CharField(max_length=5, choices=settings.LANGUAGES[1:], default=settings.LANGUAGES[0][0])
    title = models.CharField(_('title'), max_length=200, help_text=_('Page title'))
    content = models.TextField(_('content'), blank=True, help_text=_('Page content'))
    keywords = models.CharField(_('keywords'), max_length=255, help_text=_('Page keywords'))
    description = models.CharField(_('description'), max_length=255, help_text=_('Page description'))

    class Meta(object):
        # ensures we can only have on translation for each language for each page
        unique_together = (('front_page_instance', 'language'),)

    def __unicode__(self):
        return u'%s' % self.language


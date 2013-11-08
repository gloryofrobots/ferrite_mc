from django.db import models
from filebrowser.fields import FileBrowseField
#TODO change product.serie to product.series
#TODO add long_name to Type

from django.utils.translation import ugettext_lazy as _
from mothertongue.models import MothertongueModelTranslate
from tinymce import models as tinymce_models
from django.conf import settings


class Category(MothertongueModelTranslate):
    name = models.CharField(max_length=255)

    translations = models.ManyToManyField('CategoryTranslation', blank=True, verbose_name=_('category translations'))
    translation_set = 'categorytranslation_set'
    translated_fields = ['name']
    def __unicode__(self):
        return u'%s' % (self.name)

# chunks translations model
class CategoryTranslation(models.Model):
    category_instance = models.ForeignKey('Category', verbose_name=_('category_instance'))
    language = models.CharField(max_length=5, choices=settings.LANGUAGES[1:],default=settings.LANGUAGES[0][0])
    name = models.CharField(max_length=255, help_text='Category name')


    class Meta(object):
        # ensures we can only have on translation for each language for each page
        unique_together = (('category_instance', 'language'),)

    def __unicode__(self):
        return u'%s,%s' % (self.language,self.name)



class Series(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    def __unicode__(self):
        return u'%s' % (self.name)

class Type(MothertongueModelTranslate):
    name = models.CharField(max_length=255, help_text=_('Product type name'))
    long_name = models.CharField(max_length=255, help_text=_('Product type long name'))
    magic_attribute = models.CharField(max_length=255, help_text=_('Product magic attribute name'))
    direct_flow_image = FileBrowseField("Image", max_length=200, directory="images/", extensions=[".jpg", ".jpeg", ".png"],
                            blank=True, null=True, help_text=_('Direct flow image'))
    reverse_flow_image = FileBrowseField("Image", max_length=200, directory="images/",
                                        extensions=[".jpg", ".jpeg", ".png"],
                                        blank=True, null=True, help_text=_('Reverse flow image'))

    translations = models.ManyToManyField('TypeTranslation', blank=True, verbose_name=_('type translations'))
    translation_set = 'typetranslation_set'
    translated_fields = ['name','long_name','magic_attribute']

    def __unicode__(self):
        return u'%s' % (self.name)

# chunks translations model
class TypeTranslation(models.Model):
    type_instance = models.ForeignKey('Type', verbose_name=_('type_instance'))
    language = models.CharField(max_length=5, choices=settings.LANGUAGES[1:], default=settings.LANGUAGES[0][0])
    name = models.CharField(max_length=255, help_text=_('Product type name'))
    magic_attribute = models.CharField(max_length=255, help_text=_('Product magic attribute name'))
    long_name = models.CharField(max_length=255, help_text=_('Product type long name'))

    class Meta(object):
        # ensures we can only have on translation for each language for each page
        unique_together = (('type_instance', 'language'),)

    def __unicode__(self):
        return u'%s,%s' % (self.language,self.name)


class Product(MothertongueModelTranslate):
    series = models.ForeignKey(Series)
    type = models.ForeignKey(Type)
    name = models.CharField(max_length=100)
    description = tinymce_models.HTMLField(_('description'), blank=True, help_text=_('Product description'))
    frequency_min = models.FloatField()
    frequency_max = models.FloatField()
    insertion_losses_max = models.FloatField()
    insertion_losses_min = models.FloatField()
    inverse_losses_max = models.FloatField()
    inverse_losses_min = models.FloatField()
    vswr = models.FloatField()
    temperature_max = models.FloatField()
    temperature_min = models.FloatField()
    input_power = models.FloatField()
    reflected_power = models.FloatField()
    soldering_temperature = models.FloatField()
    peak_temperature = models.FloatField()
    permittivity = models.FloatField()
    wave_resistance = models.FloatField()
    price = models.FloatField()

    translations = models.ManyToManyField('ProductTranslation', blank=True, verbose_name=_('product translations'))
    translation_set = 'producttranslation_set'
    translated_fields = ['description']

    def __unicode__(self):
        return u'%s-%s' % (self.series, self.name)

class ProductTranslation(models.Model):
    product_instance = models.ForeignKey('Product', verbose_name=_('product_instance'))
    language = models.CharField(max_length=5, choices=settings.LANGUAGES[1:], default=settings.LANGUAGES[0][0])
    description = tinymce_models.HTMLField(_('description'), blank=True, help_text=_('Product description'))


    class Meta(object):
        # ensures we can only have on translation for each language for each page
        unique_together = (('product_instance', 'language'),)

    def __unicode__(self):
        return u'%s' % self.language

class ProductImage(models.Model):
    image = FileBrowseField("Image", max_length=200, directory="images/", extensions=[".jpg", ".jpeg", ".png"],
                            blank=True, null=True)
    product = models.ForeignKey(Product)

    def __unicode__(self):
        return u'%s' % str(self.image)

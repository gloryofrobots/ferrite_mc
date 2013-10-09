# import stuff we need from django
from django.contrib import admin
# import stuff we need from django
# import app specific shit
from products.models import Product,ProductImage,ProductTranslation,Serie,Type,TypeTranslation,Category,CategoryTranslation
from django.conf import settings
"""
class Serie(models.Model):
    name = models.CharField(max_length=100)

class Type(MothertongueModelTranslate):
    name = models.CharField(max_length=255, help_text='Product type name')
    direct_flow_image = FileBrowseField("Image", max_length=200, directory="images/", extensions=[".jpg", ".jpeg", ".png"],
                            blank=True, null=True, help_text='Direct flow image')
    reverse_flow_image = FileBrowseField("Image", max_length=200, directory="images/",
                                        extensions=[".jpg", ".jpeg", ".png"],
                                        blank=True, null=True, help_text='Reverse flow image')

    translations = models.ManyToManyField('TypeTranslation', blank=True, verbose_name=_('type translations'))
    translation_set = 'type_translation_set'
    translated_fields = ['name']

# chunks translations model
class TypeTranslation(models.Model):
    type_instance = models.ForeignKey('Type', verbose_name=_('type_instance'))
    language = models.CharField(max_length=5, choices=settings.LANGUAGES[1:])
    name = models.CharField(max_length=255, help_text='Product type name')


    class Meta(object):
        # ensures we can only have on translation for each language for each page
        unique_together = (('type_instance', 'language'),)

    def __unicode__(self):
        return u'%s,%s' % self.language,self.name


class Product(MothertongueModelTranslate):
    serie = models.ForeignKey(Serie)
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
    temperature_max = models.IntegerField()
    temperature_min = models.IntegerField()
    input_power = models.FloatField()

    translations = models.ManyToManyField('ProductTranslation', blank=True, verbose_name=_('product translations'))
    translation_set = 'product_translation_set'
    translated_fields = ['description']



"""





class ProductTranslationInline(admin.StackedInline):
    model = ProductTranslation
    extra = 1
    max_num = len(settings.LANGUAGES)-1

    fieldsets = (
        (None, {
            'fields': ['language',]
        }),
        ('Translation', {
            'fields': ['description'],
            'classes': ['collapse',],
        }),
    )
    #formfield_overrides = {
    #    models.TextField: {'widget': TinyMCE},
    #}

class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1
    max_num = 3
    fields = ['image']
    #formfield_overrides = {
    #    models.TextField: {'widget': TinyMCE},
    #}

class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductTranslationInline,ProductImageInline)
    fields = ['serie','type','name','description',
              'frequency_min','frequency_max','insertion_losses_min','insertion_losses_max',
              'inverse_losses_min','inverse_losses_max','vswr','temperature_min','temperature_max','input_power']


class TypeTranslationInline(admin.StackedInline):
    model = TypeTranslation
    extra = 1
    max_num = len(settings.LANGUAGES)-1

    fieldsets = (
        (None, {
            'fields': ['language',]
        }),
        ('Translation', {
            'fields': ['name'],
            'classes': ['collapse',],
        }),
    )

class TypeAdmin(admin.ModelAdmin):
    fields = ['name','direct_flow_image','reverse_flow_image']
    inlines = (TypeTranslationInline,)

class CategoryTranslationInline(admin.StackedInline):
    model = CategoryTranslation
    extra = 1
    max_num = len(settings.LANGUAGES)-1

    fieldsets = (
        (None, {
            'fields': ['language',]
        }),
        ('Translation', {
            'fields': ['name'],
            'classes': ['collapse',],
        }),
    )

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    inlines = (CategoryTranslationInline,)


class SeriesProductInline(admin.StackedInline):
    model = Product
    extra = 0
    fields = ['type', 'name', 'description',
              'frequency_min', 'frequency_max', 'insertion_losses_max', 'insertion_losses_min',
              'inverse_losses_max', 'inverse_losses_min', 'vswr', 'temperature_max', 'temperature_min', 'input_power']
    #formfield_overrides = {
    #    models.TextField: {'widget': TinyMCE},
    #}


class SeriesAdmin(admin.ModelAdmin):
    fields = ['name','category']
    inlines = (SeriesProductInline,)

# register with CMS
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Serie, SeriesAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Category, CategoryAdmin)
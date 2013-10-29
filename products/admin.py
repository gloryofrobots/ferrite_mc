# import stuff we need from django
from django.contrib import admin
# import stuff we need from django
# import app specific shit
from products.models import Product, ProductImage, ProductTranslation, Series, Type, TypeTranslation, Category, CategoryTranslation
from django.conf import settings


class ProductTranslationInline(admin.StackedInline):
    model = ProductTranslation
    extra = 1
    max_num = len(settings.LANGUAGES) - 1

    inline_classes = ('grp-collapse grp-open',)
    fieldsets = (
        (None, {
            'fields': ['language', ]
        }),
        ('Translation', {
            'fields': ['description'],
            #'classes': ['collapse',],
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

    inline_classes = ('grp-collapse grp-open',)
    #formfield_overrides = {
    #    models.TextField: {'widget': TinyMCE},
    #}


class ProductAdmin(admin.ModelAdmin):
    #def upper_case_name(obj):
    #    return ("%s %s" % (obj.series.name, obj.name))
    #
    #upper_case_name.short_description = 'Name'

    inlines = (ProductTranslationInline, ProductImageInline)
    fields = ['series', 'type', 'name', 'description',
              'frequency_min', 'frequency_max', 'insertion_losses_min', 'insertion_losses_max',
              'inverse_losses_min', 'inverse_losses_max', 'vswr', 'temperature_min', 'temperature_max', 'input_power']
    list_display = ( 'name', 'series', 'type', 'frequency_min', 'frequency_max')
    list_filter = ('series', 'type', 'frequency_min', 'frequency_max')


class TypeTranslationInline(admin.StackedInline):
    model = TypeTranslation
    extra = 1
    max_num = len(settings.LANGUAGES) - 1
    inline_classes = ('grp-collapse grp-open',)
    fieldsets = (
        (None, {
            'fields': ['language', ]
        }),
        ('Translation', {
            'fields': ['name', 'long_name'],
        }),
    )


class TypeAdmin(admin.ModelAdmin):
    fields = ['name', 'long_name', 'direct_flow_image', 'reverse_flow_image']
    inlines = (TypeTranslationInline,)


class CategoryTranslationInline(admin.StackedInline):
    model = CategoryTranslation
    extra = 1
    max_num = len(settings.LANGUAGES) - 1

    inline_classes = ('grp-collapse grp-open',)

    fieldsets = (
        (None, {
            'fields': ['language', ]
        }),
        ('Translation', {
            'fields': ['name'],
        }),
    )


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    inlines = (CategoryTranslationInline,)


class SeriesProductInline(admin.StackedInline):
    model = Product
    extra = 1
    fields = ['type', 'name', 'description',
              'frequency_min', 'frequency_max', 'insertion_losses_min', 'insertion_losses_max',
              'inverse_losses_min', 'inverse_losses_max', 'vswr', 'temperature_min', 'temperature_max', 'input_power']


class SeriesAdmin(admin.ModelAdmin):
    fields = ['name', 'category']
    inlines = (SeriesProductInline,)

# register with CMS
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Category, CategoryAdmin)
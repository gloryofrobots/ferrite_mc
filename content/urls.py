__author__ = 'gloryofrobots'
from django.conf.urls import patterns, include, url

from django.conf import settings



urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'content.views.show_main', name='main'),
                       url(r'^category/(?P<category_id>\d+)$', 'content.views.show_category', name="show_category"),
                       url(r'^series/(?P<series_id>\d+)$', 'content.views.show_series', name='show_series'),
                       url(r'^product/(?P<product_id>\d+)$', 'content.views.show_product', name = "show_product"),
                       url(r'^page/(?P<alias>\w+)$', 'content.views.show_page', name="show_page"),
)

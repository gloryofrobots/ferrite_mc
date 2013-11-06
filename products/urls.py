__author__ = 'gloryofrobots'
from django.conf.urls import patterns, include, url

from django.conf import settings



urlpatterns = patterns('',
                       url(r'^secretpage_set_product_images/(?P<password>\d+)$', 'products.views.auto_set_product_images',
                           name="auto_set_product_images")

)

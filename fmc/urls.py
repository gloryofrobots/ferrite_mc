from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from filebrowser.sites import site

admin.autodiscover()
from content.urls import urlpatterns as content_paterns

urlpatterns = patterns('',
                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.MEDIA_ROOT}),
                        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.STATIC_ROOT}),
		      (r'^products/', include('products.urls')), # grappelli URLS
                       (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
                       (r'^admin/', include(admin.site.urls)), # admin site
                       url(r'^admin/filebrowser/', include(site.urls)),
                       (r'^tinymce/', include('tinymce.urls')),


)
urlpatterns += content_paterns

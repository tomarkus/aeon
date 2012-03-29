from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'aeon.blog.views.index', name='index'),
    url(r'^about/$', 'aeon.blog.views.about', name='about'),
    url(r'^music/$', 'aeon.blog.views.music', name='music'),
    url(r'^contact/$', 'aeon.blog.views.contact', name='contact'),
    # url(r'^aeon/', include('aeon.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

)


urlpatterns += staticfiles_urlpatterns()
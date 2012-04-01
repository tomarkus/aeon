from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'aeon.blog.views.index',
        name='index'),
    url(r'^(?P<slug>.*)/(?P<pk>\d+)/$', 'aeon.blog.views.post_detail',
        name='post_detail'),
    url(r'^about/$', 'aeon.blog.views.about', name='about'),
    url(r'^music/$', 'aeon.blog.views.music', name='music'),
    url(r'^contact/$', 'aeon.blog.views.contact', name='contact'),

)


urlpatterns += staticfiles_urlpatterns()
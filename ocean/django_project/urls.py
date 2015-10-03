from django.conf.urls import patterns, include, url
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', views.index, name='index'),
    url(r'^bible$',   'doc.views.bible'),
    url(r'^prayers$', 'doc.views.prayers'),
    url(r'^reflect$', 'doc.views.prayers'),
    url(r'^review$',  'doc.views.prayers'),
    url(r'^',         include('doc.urls')),
)


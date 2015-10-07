from django.conf.urls import patterns, include, url
from django.contrib import admin
from os.path import join


admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^$',                              'doc.views.home'),
    url(r'^bible$',                         'doc.views.bible'),
    url(r'^prayers$',                       'doc.views.prayers'),
    url(r'^reflect$',                       'doc.views.reflect'),
    url(r'^review$',                        'doc.views.review'),
    url(r'^(?P<title>[\w\-_./]+).asc$',     'doc.views.asciidoc'),
    url(r'^(?P<title>[\w\-_./]+)/new$',     'doc.views.new'),
    url(r'^(?P<title>[\w\-_./]+)/missing$', 'doc.views.missing'),
    url(r'^(?P<title>[\w\-_./]+)/add$',     'doc.views.add'),
    url(r'^(?P<title>[\w\-_./]+)/edit$',    'doc.views.edit'),
    url(r'^(?P<title>[\w\-_./]+)/delete$',  'doc.views.delete'),
    url(r'^(?P<title>[\w\-_./]+)$',         'doc.views.doc'),

)

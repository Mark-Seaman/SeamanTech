from django.conf.urls import patterns, include, url
from django.contrib import admin
from os.path import join


admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^$',         'doc.notes.home'),

    url(r'bible$',     'doc.spiritual.bible'),
    url(r'prayers$',   'doc.spiritual.prayers'),
    url(r'reflect$',   'doc.spiritual.reflect'),
    url(r'review$',    'doc.spiritual.review'),
    # url(r'^spiritual/(?P<title>[\w\/\-_./]+)',  'doc.notes.spiritual'),

    # url(r'^notes/(?P<title>[\w\/\-_./]+)',      'doc.notes.notes'),

    # url(r'^tech/(?P<title>[\w\/\-_./]+)',       'doc.notes.tech'),
    
    # url(r'^Leverage/(?P<title>[\w\/\-_./]+)',   'doc.notes.leverage'),

    # #url(r'^brain/(?P<title>[\w\/\-_./]+)',      'doc.notes.brain'),

    # url(r'^seamanslog/(?P<title>[\w\/\-_./]+)', 'doc.notes.seamanslog'),

    url(r'^(?P<title>[\w\/\-_./]+)',            'doc.notes.doc'),

    # url(r'^(?P<title>[\w\-_./]+).asc$',         'doc.views.asciidoc'),
    # url(r'^(?P<title>[\w\-_./]+)/new$',         'doc.views.new'),
    # url(r'^(?P<title>[\w\-_./]+)/missing$',     'doc.views.missing'),
    # url(r'^(?P<title>[\w\-_./]+)/add$',         'doc.views.add'),
    # url(r'^(?P<title>[\w\-_./]+)/edit$',        'doc.views.edit'),
    # url(r'^(?P<title>[\w\-_./]+)/delete$',      'doc.views.delete'),
    # url(r'^(?P<title>[\w\-_./]+)$',             'doc.views.doc'),

)

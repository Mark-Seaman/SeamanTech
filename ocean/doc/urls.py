from django.conf.urls import patterns, include, url
from django.contrib import admin
from os.path import join


admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'bible$',     'doc.spiritual.bible'),
    url(r'prayers$',   'doc.spiritual.prayers'),
    url(r'reflect$',   'doc.spiritual.reflect'),
    url(r'review$',    'doc.spiritual.review'),

    url(r'^thots$',                     'doc.notes.thots'),
    url(r'^get_thot$',                  'doc.notes.get_thot'),
    url(r'^put_thot$',                  'doc.notes.put_thot'),

    url(r'^$',                          'doc.notes.home'),
    url(r'^notes/Church/budgetcalc$',   'doc.notes.budget'),
    url(r'^(?P<title>[\w\/\-_./]+)',    'doc.notes.doc'),
)

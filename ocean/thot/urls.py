from django.conf.urls import patterns, include, url
from django.contrib import admin
from os.path import join


admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^$',           'thot.views.thots'),
    url(r'^get_thot$',   'thot.views.get_thot'),
    url(r'^put_thot$',   'thot.views.put_thot'),
)

# app/urls.py
# Routes to views

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',  
    url(r'^$', 'app.views.home', name='/'),
    url(r'^user$', 'app.views.user', name='user'),
    url(r'^test$', 'app.views.test_view', name='test'),
    url(r'^no_access$', 'app.views.no_access'),

    (r'^login', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),  
    (r'^logout', 'app.views.logout_view'),

    url(r'^doc', include('doc.urls')),
)

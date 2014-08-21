# app/urls.py
# Routes to views

from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',

    # login
    (r'^login', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),  
    (r'^logout', 'app.views.logout_view'),

    # doc
    url(r'^',         include('doc.urls')),

    # task
    url(r'^project/', include('task.project_urls')),
    url(r'^time/',    include('task.time_urls')),

    # other

    url(r'^home$', 'app.views.home', name='/'),
    url(r'^user$', 'app.views.user', name='user'),
    url(r'^test$', 'app.views.test_view', name='test'),
    url(r'^no_access$', 'app.views.no_access'),


)

# urls_dt.py
# Time urls

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from time_views   import TimeList, TimeDetail, TimeAdd, TimeEdit, TimeDelete


urlpatterns = patterns(
    '',

    # Time  (List, Detail, Add, Edit, Delete, Test)

    #Home
    url(r'^$',                    TemplateView.as_view(template_name="time.html")),
    
    # List
    url(r'^/$',                   TimeList.as_view(), name='time_list'),
    
    # Detail
    url(r'^/(?P<pk>\d+)$',        TimeDetail.as_view(), name='time-detail'),

    # Add
    url(r'^/add$',                login_required(TimeAdd.as_view(), login_url='/login'), name='time_add'),

    # Edit
    url(r'^/(?P<pk>\d+)/edit$',   login_required(TimeEdit.as_view(), login_url='/login'), name='time_update'),

    # Delete
    url(r'^/(?P<pk>\d+)/delete$', login_required(TimeDelete.as_view(), login_url='/login'),
        name='time_delete'),

    # Test
    url(r'^/test$',               login_required(TemplateView.as_view(template_name="time_test.html"), login_url='/login')),

    # Catch all view
    url(r'^',                     TemplateView.as_view(template_name="missing.html")),

)

# urls_dt.py
# Data_Type urls

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from data_type_views   import Data_TypeList, Data_TypeDetail, Data_TypeAdd, Data_TypeEdit, Data_TypeDelete


urlpatterns = patterns(
    '',

    # Data_Type  (List, Detail, Add, Edit, Delete, Test)

    #Home
    url(r'^$',                    TemplateView.as_view(template_name="data_type.html")),
    
    # List
    url(r'^/$',                   Data_TypeList.as_view(), name='data_type_list'),
    
    # Detail
    url(r'^/(?P<pk>\d+)$',        Data_TypeDetail.as_view(), name='data_type-detail'),

    # Add
    url(r'^/add$',                login_required(Data_TypeAdd.as_view(), login_url='/login'), name='data_type_add'),

    # Edit
    url(r'^/(?P<pk>\d+)/edit$',   login_required(Data_TypeEdit.as_view(), login_url='/login'), name='data_type_update'),

    # Delete
    url(r'^/(?P<pk>\d+)/delete$', login_required(Data_TypeDelete.as_view(), login_url='/login'),
        name='data_type_delete'),

    # Test
    url(r'^/test$',               login_required(TemplateView.as_view(template_name="data_type_test.html"), login_url='/login')),

    # Catch all view
    url(r'^',                     TemplateView.as_view(template_name="missing.html")),

)

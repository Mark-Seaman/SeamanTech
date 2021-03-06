# urls_dt.py
# Contact urls


#############################################################################
# DO NOT EDIT THIS FILE
# This Code will be replaced by the code generator
#############################################################################

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from contact_views   import ContactList, ContactDetail, ContactAdd, ContactEdit, ContactDelete


urlpatterns = patterns(
    '',

    # Contact  (List, Detail, Add, Edit, Delete, Test)

    #Home
    url(r'^$',                    TemplateView.as_view(template_name="contact.html")),
    
    # List
    url(r'^/$',                   ContactList.as_view(), name='contact_list'),
    
    # Detail
    url(r'^/(?P<pk>\d+)$',        ContactDetail.as_view(), name='contact-detail'),

    # Add
    url(r'^/add$',                login_required(ContactAdd.as_view(), login_url='/login'), name='contact_add'),

    # Edit
    url(r'^/(?P<pk>\d+)/edit$',   login_required(ContactEdit.as_view(), login_url='/login'), name='contact_update'),

    # Delete
    url(r'^/(?P<pk>\d+)/delete$', login_required(ContactDelete.as_view(), login_url='/login'),
        name='contact_delete'),

    # Test
    url(r'^/test$',               login_required(TemplateView.as_view(template_name="contact_test.html"), login_url='/login')),

    # Catch all view
    url(r'^',                     TemplateView.as_view(template_name="missing.html")),

)

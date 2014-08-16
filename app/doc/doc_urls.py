# urls_dt.py
# Doc urls

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from doc_views   import DocList, DocDetail, DocAdd, DocEdit, DocDelete


urlpatterns = patterns(
    '',

    # Doc  (List, Detail, Add, Edit, Delete, Test)

    #Home
    url(r'^$',                    TemplateView.as_view(template_name="doc.html")),
    
    # List
    url(r'^/$',                   DocList.as_view(), name='doc_list'),
    
    # Detail
    url(r'^/(?P<pk>\d+)$',        DocDetail.as_view(), name='doc-detail'),

    # Add
    url(r'^/add$',                login_required(DocAdd.as_view(), login_url='/login'), name='doc_add'),

    # Edit
    url(r'^/(?P<pk>\d+)/edit$',   login_required(DocEdit.as_view(), login_url='/login'), name='doc_update'),

    # Delete
    url(r'^/(?P<pk>\d+)/delete$', login_required(DocDelete.as_view(), login_url='/login'),
        name='doc_delete'),

    # Test
    url(r'^/test$',               login_required(TemplateView.as_view(template_name="doc_test.html"), login_url='/login')),

    # Catch all view
    url(r'^',                     TemplateView.as_view(template_name="missing.html")),

)

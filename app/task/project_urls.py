# urls_dt.py
# Project urls

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from project_views   import ProjectList, ProjectDetail, ProjectAdd, ProjectEdit, ProjectDelete


urlpatterns = patterns(
    '',

    # Project  (List, Detail, Add, Edit, Delete, Test)

    #Home
    url(r'^$',                    TemplateView.as_view(template_name="project.html")),
    
    # List
    url(r'^/$',                   ProjectList.as_view(), name='project_list'),
    
    # Detail
    url(r'^/(?P<pk>\d+)$',        ProjectDetail.as_view(), name='project-detail'),

    # Add
    url(r'^/add$',                login_required(ProjectAdd.as_view(), login_url='/login'), name='project_add'),

    # Edit
    url(r'^/(?P<pk>\d+)/edit$',   login_required(ProjectEdit.as_view(), login_url='/login'), name='project_update'),

    # Delete
    url(r'^/(?P<pk>\d+)/delete$', login_required(ProjectDelete.as_view(), login_url='/login'),
        name='project_delete'),

    # Test
    url(r'^/test$',               login_required(TemplateView.as_view(template_name="project_test.html"), login_url='/login')),

    # Catch all view
    url(r'^',                     TemplateView.as_view(template_name="missing.html")),

)

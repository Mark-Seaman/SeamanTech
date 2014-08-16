# urls_dt.py
# Note urls

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from note_views   import NoteList, NoteDetail, NoteAdd, NoteEdit, NoteDelete


urlpatterns = patterns(
    '',

    # Note  (List, Detail, Add, Edit, Delete, Test)

    #Home
    url(r'^$',                    TemplateView.as_view(template_name="note.html")),
    
    # List
    url(r'^/$',                   NoteList.as_view(), name='note_list'),
    
    # Detail
    url(r'^/(?P<pk>\d+)$',        NoteDetail.as_view(), name='note-detail'),

    # Add
    url(r'^/add$',                login_required(NoteAdd.as_view(), login_url='/login'), name='note_add'),

    # Edit
    url(r'^/(?P<pk>\d+)/edit$',   login_required(NoteEdit.as_view(), login_url='/login'), name='note_update'),

    # Delete
    url(r'^/(?P<pk>\d+)/delete$', login_required(NoteDelete.as_view(), login_url='/login'),
        name='note_delete'),

    # Test
    url(r'^/test$',               login_required(TemplateView.as_view(template_name="note_test.html"), login_url='/login')),

    # Catch all view
    url(r'^',                     TemplateView.as_view(template_name="missing.html")),

)

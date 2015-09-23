# note/views_dt.py
# Note views for basic operations


#############################################################################
# DO NOT EDIT THIS FILE
# This Code will be replaced by the code generator
#############################################################################

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required

from note_model import Note
from note_query import query_note, get_note


# Basic list view with using a template
class NoteList(ListView):
    model = Note
    template_name = 'note_list.html'

    # Filter the list of choices
    queryset = query_note()

    # Use the request user to match the items
    #def get_queryset(self):
    #    return Note.objects.filter(name=self.request.user.username)


# Basic detail view
class NoteDetail(DetailView):
    model = Note
    template_name = 'note_detail.html'

    # Call the base implementation first to get a context
    def get_context_data(self, **kwargs):
        context = super(NoteDetail, self).get_context_data(**kwargs)
        id = context['object'].pk
        context['value_list'] = get_note(self.request.user,id)
        return context


# Create view
class NoteAdd(CreateView):
    model = Note
    template_name = 'note_edit.html'


# Update view
class NoteEdit(UpdateView):
    model = Note
    template_name = 'note_edit.html'


# Delete view
class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('note_list')
    template_name = 'note_delete.html'


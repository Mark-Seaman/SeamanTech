from datetime           import datetime
from django.contrib.auth.decorators import login_required
from django.http        import HttpResponseRedirect, HttpResponse
from django.shortcuts   import render_to_response, get_object_or_404
from django.template    import loader, Context, RequestContext
from django.utils.html  import escape
from os.path            import join, exists, dirname
from os                 import system,environ, listdir
from random import choice

from models    import *
from util.domain import domain_title
from util.page import doc_path, show_page,  put_page, get_page, page_redirect, allow_edit
from util.log  import append_log
from doc.asciidoc import asciidoc_html
from django_project.settings import DOC_ROOT


def random_select(request,topic):
    '''Select content from a random file in the directory'''
    path = '%s/Public/Spiritual-Things.org/%s'% (DOC_ROOT,topic)
    select = choice(listdir(path))
    return redirect(request,topic+'/'+select)


def random_file(topic):
    '''Select content from a random file in the directory'''
    path = '%s/Public/Spiritual-Things.org/%s'% (DOC_ROOT,topic)
    select = choice(listdir(path))
    path = join(path,select)
    text = open(path).read()
    return '<h3>%s</h3><br><p>%s</p>' % (text,select)


def random_line(topic):
    path = '%s/Public/Spiritual-Things.org/%s'% (DOC_ROOT,topic)
    # text = '<h3>%s</h3>' % choice(open(path).read().split('\n'))
    # title = 'Reflection'
    # return render_page (request,title,text)
    return '<h3>%s</h3>' % choice(open(path).read().split('\n'))


# def random_page(request, topic):
#     text = random_file(request,topic)
#     title = topic
#     return render_page (request,title,text)


def bible(request):
    return render_page (request, 'bible', random_file('bible'))

def reflect(request):
    return render_page (request, 'reflection', random_line('reflection/Questions'))

def review(request):
    return random_select(request, 'teaching')

def prayers(request):
    return random_select(request, 'prayers')


def asciidoc(request,title):
    '''Find and render to asciidoc content'''
    host = request.get_host()
    doc  = doc_path(host,'Public',title+'.asc')
    text = asciidoc_html(doc)
    site_title = domain_title(host)
    return render_page(request,title,text)


def doc(request,title):
    '''Render the appropriate doc view'''
    doc = user_doc(request,title)
    log_page (request, title)
    host = request.get_host()
    u = user(request)
    p = page_redirect(host,u,title)
    if p: 
        return redirect(request,p)
    text = show_page(host,u,title,True)
    return render_page(request,title,text)


def render_page(request,title,text):
    '''Format the web page with content'''
    site = domain_title(request.get_host())
    content =  {
        'site_title': site, 
        'user': request.user, 
        'title': site + '-' +title, 
        'text': text
    }
    return render(request, 'doc.html', content)


# Render a web page
def render(request,template,data): 
    page = loader.get_template (template)
    return HttpResponse(page.render(Context(data)))


# Render a form for editing
def form_render(request,template,data):
    return render_to_response(template, data, context_instance=RequestContext(request))


# Name of requesting user
def user(request):
    if not request.user.is_anonymous():
        return request.user.username
    else:
        return 'Anonymous'


# Return the document for this user.
def user_doc(request,title):
    host = request.get_host()
    username = user(request)
    return join(host,username,title)


# Log the page hit in page.log  (time, ip, user, page, doc) 
def log_page(request,title): 
    append_log(request.get_host()+' '+user(request)+' '+title)


# Render the view for a missing document
def new(request,title):
    text = 'Creating a new page,'+title
    data = {'title':title, 'dir':dirname(title), 'text':text, 
            'default':basename(title), 'newpage':'{{newpage}}'}
    return render(request, 'new.html', data)


# Render the view for a missing document
def missing(request,title):
    text = 'Missing File:' + title
    text = user_doc(request,title)
    data = {'title':title, 'dir':dirname(title), 'text':text, 
            'default':basename(title), 'newpage':'{{newpage}}'}
    return render(request, 'missing.html', data)


# Go to a specific page
def redirect(request,title):
    log_page (request,title)
    return HttpResponseRedirect('/'+title) 


# Render the home view
def home(request):
    return  doc(request,'Index')


# Render the home view
def signup(request,listname):

    text = '''Get updates automatically by email.<br>
<br>
It's free, and easy.<br>
<br>
Unsubscribe at any time.<br>'''
    if listname=='MyBookOnline':
        form = 'signup.html'
    else:
        form = 'signup-seamanslog.html'

    return  render(request, form, {'title': listname, 'text': text })


@login_required(login_url='/login')
def private(request,title):
    return doc(request,title)


#-----------------------------------------------------------------------------
# Edit


# Get and put doc directly
@login_required(login_url='/login')
def read_text(request,title,text):
    log_page (request,'read:%s'%title)
    if not text:
        text = get_page(request.get_host(),user(request),title)
    return text


# Save the text after editing
def save_text(request,title,text):
    log_page (request, 'save:%s'%title)
    text = text.encode('ascii', 'ignore')
    text = text.replace('\r','')
    host = request.get_host()
    u = user(request)
    put_page(host,u,title,text)


# Create a form for editing the object details
@login_required(login_url='/login')
def edit_form (request, doc, title=None, text=None):
    log_page (request, 'form:%s'%doc)
    #return missing(request,title)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if request.POST.get('cancel', None):
            return redirect(request,title)
        else:
            if form.is_valid():
                text =  form.cleaned_data['body']
                save_text(request,title,text)
                return redirect(request,title)
    else:
        note =  Note()
        note.path = title
        note.body = read_text(request,title,text)
        form =  NoteForm(instance=note)

    data =  { 'form': form, 'title': title, 'banner': True  }
    return form_render (request, 'docedit.html', data)


# Render the add view
def edit(request,title):
    doc = user_doc(request,title)
    log_page (request, 'edit:%s'%doc)
    if allow_edit(request.get_host(), user(request), title):
        return edit_form (request, doc, title)
    else:
        return missing(request,"NOT ALLOWED TO EDIT -- "+title)


# Render the add view
def add(request,title):
    log_page (request,'add:%s'%title)
    return missing(request,title)
    text = add_doc(user_doc(request,title))
    if text.startswith('redirect:'):
        return redirect(request,text[len('redirect:'):-1])
    return missing(request,title)

# Delete a specific document
def delete(request,title):
    '''
    Delete the record
    '''
    doc = user_doc(request,title)
    log_page (request, 'delete: %s'%title)
    return missing(request,title)
    delete_doc (doc)
    return redirect(request,dirname(title))


# Check for all security violations
def permitted(request,title=''):
    return title.startswith('Anonymous') or user(request)!='Anonymous'


# Check for permissions
def illegal(request):
    title = 'IllegalMachine'
    log_page (request, 'illegal: %s'%title)
    user = str(request.user)
    text = user+format_doc(title)%ip(request)
    return render(request, 'doc.html', {'title': title, 'text': text})

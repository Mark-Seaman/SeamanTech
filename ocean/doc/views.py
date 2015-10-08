from django.http        import HttpResponseRedirect, HttpResponse
from django.template    import loader, Context
from os import system, environ, listdir
from os.path import join, exists
from random import choice

from util.domain import domain_title
from util.page import doc_path, show_page,  put_page, get_page, page_redirect 
from util.log  import append_log
from doc.asciidoc import asciidoc_html
from util.tabs  import format_tabs, format_doc


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

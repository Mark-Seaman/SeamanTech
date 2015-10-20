from os import listdir
from os.path import join, exists, isdir
from subprocess import Popen,PIPE

from django.http        import HttpResponseRedirect, HttpResponse
from django.template    import loader, Context
from os import system, environ, listdir
from os.path import join, exists, dirname, basename
from random import choice

from django_project.settings import DOC_ROOT
from util.log import append_log
from util.domain import domain_directory, domain_title


def random_select(request, topic):
    '''Select content from a random file in the directory'''
    path = join(DOC_ROOT, topic)
    select = choice(listdir(path)).replace('.md','')
    return redirect(request, join(topic, select))


def random_file(topic):
    '''Select content from a random file in the directory'''
    path = join(DOC_ROOT, topic)
    select = choice(listdir(path))
    path = join(path,select)
    text = open(path).read()
    return '<h3>%s</h3><br><p>%s</p>' % (text,select)


def random_line(topic):
    path = join(DOC_ROOT, topic)
    return '<h3>%s</h3>' % choice(open(path).read().split('\n'))


#----------------------------------------------------------------------

def redirect(request,title):
    '''Go to a specific page'''
    append_log (join(request.get_host(), title))
    return HttpResponseRedirect('/'+title) 


def render_page(request,title,text):
    '''Format the web page with content'''
    site = domain_title(request.get_host())
    content =  {
        'site_title': site, 
        'document': title,
        'user': request.user, 
        'title': site + '-' + title, 
        'text': text
    }
    page = loader.get_template ('doc.html')
    return HttpResponse(page.render(Context(content)))


def is_document (request,title):
    '''Check to see if the document exists'''
    host = request.get_host()
    path = join(DOC_ROOT,host,title)
    return exists(path+'.md')


def render_doc_html(path):
    '''Render the HTML for the doc content'''
    if exists(path+'.md'):
        script = ['pandoc', '-t', 'html', path+'.md']
        output = Popen(script, stdout=PIPE).stdout
        return output.read().decode(encoding='UTF-8')
    else:
        return ("Path NOT found "+path)


# def render_document_page (request,title):
#     '''If the note is a directory or a file display it'''
#     append_log (join(request.get_host(), title))
#     path = join(DOC_ROOT, title)
#     text = render_doc_html(path)
#     return render_page(request,title,text)


# def page(request, title, docdir):
#     append_log (join(request.get_host(), docdir, title))
#     path = join(DOC_ROOT, docdir, title)
#     text = render_doc_html(path)
#     return render_page(request, title, text)

def doc(request,title):
    '''If the note is a directory or a file display it'''
    append_log (join(request.get_host(), title))
    path = join(DOC_ROOT, title)
    text = render_doc_html(path)
    return render_page(request, title, text)

 

# def seamanslog(request,title):
#     '''If the note is a directory or a file display it'''
#     if title=='Index':
#         return random_select(request,'seamanslog')
#     return page(request, title, 'seamanslog')

# def brain(request,title):
#     '''If the note is a directory or a file display it'''
#     return page(request, title, 'brain')

# def tech(request,title):
#     '''If the note is a directory or a file display it'''
#     return page(request, title, 'tech')


# def spiritual(request,title):
#     '''If the note is a directory or a file display it'''
#     return page(request, title, 'spiritual')


# def leverage(request,title):
#     '''If the note is a directory or a file display it'''
#     return page(request, title, 'Leverage')


# def notes(request,title):
#     '''If the note is a directory or a file display it'''
#     return page(request, title, 'Notes')


def notes_directory(path,title):
    '''Display the HTML text for the directory'''
    anchor = '<a href="/notes/%s/%s">%s</a>'
    files = [ anchor % (title, f, f) for f in listdir(path) ]
    return '<h1>%s</h1>' % title + '<br>'.join(files)


def home(request):
    '''Render the home view'''
    dir = domain_directory(request.get_host())
    return  redirect(request, dir+'/Index')

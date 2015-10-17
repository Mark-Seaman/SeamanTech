from os import listdir
from os.path import join, exists, isdir
from subprocess import Popen,PIPE

from django_project.settings import DOC_ROOT
from doc.views import render_page, redirect
from util.log import append_log


def is_document (request,title):
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


def render_document_page (request,title):
    '''If the note is a directory or a file display it'''
    append_log (request.get_host() + title)
    path = join(DOC_ROOT,request.get_host(),title)
    text = render_doc_html(path)
    return render_page(request,title,text)


def notes(request,title):
    '''If the note is a directory or a file display it'''
    append_log (request.get_host() + ' Notes/' + title)
    path = join(DOC_ROOT,'Notes',title)
    text = render_doc_html(path)
    return render_page(request,title,text)


def notes_directory(path,title):
    '''Display the HTML text for the directory'''
    anchor = '<a href="/notes/%s/%s">%s</a>'
    files = [ anchor % (title, f, f) for f in listdir(path) ]
    return '<h1>%s</h1>' % title + '<br>'.join(files)

from os import listdir
from os.path import join, exists, isdir

from django_project.settings import DOC_ROOT
from doc.views import render_page, redirect
from util.log import append_log
from shell import shell


def doc_html(topic):
    '''Render the HTML for the doc content'''
    path = join(DOC_ROOT,'Notes',topic)
    return shell('text html '+path)


def notes(request,title):
    '''If the note is a directory or a file display it'''
    append_log (request.get_host() + ' ' + title)
    path = join(DOC_ROOT,'Notes',title)
    if not exists(path): 
        return redirect(request,join(path,'missing'))
    if isdir(path):
        return render_page(request, title, notes_directory(path,title))
    text = doc_html(path)
    return render_page(request,title,text)


def notes_directory(path,title):
    '''Display the HTML text for the directory'''
    anchor = '<a href="/notes/%s/%s">%s</a>'
    files = [ anchor % (title, f, f) for f in listdir(path) ]
    return '<h1>%s</h1>' % title + '<br>'.join(files)

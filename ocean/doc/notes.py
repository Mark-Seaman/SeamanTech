from django.http        import HttpResponseRedirect, HttpResponse
from django.template    import loader, Context
from os import listdir
from os.path import join, exists, isdir

from django_project.settings import DOC_ROOT
from util.log import append_log
from shell import shell


def render_page(request,template,title,text):
    '''Format the web page with content'''
    content =  {
        'site_title': title, 
        'user': request.user, 
        'title': title, 
        'text': text
    }
    page = loader.get_template (template)
    return HttpResponse(page.render(Context(content)))


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
    return render_page(request,'doc.html',title,text)

def thots(request):
    return render_page(request,'thot.html', "4 thot",'{"name": "my thoughts exactly!"}')


def notes_directory(path,title):
    '''Display the HTML text for the directory'''
    anchor = '<a href="/notes/%s/%s">%s</a>'
    files = [ anchor % (title, f, f) for f in listdir(path) ]
    return '<h1>%s</h1>' % title + '<br>'.join(files)

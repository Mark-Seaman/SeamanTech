from django.http        import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template    import loader, Context
from os import system, environ, listdir
from os.path import join, exists, isdir, dirname, basename
from random import choice
from subprocess import Popen,PIPE

from django_project.settings import DOC_ROOT
from doc.log import append_log
from doc.domain import domain_directory, domain_title


def thots(request):
    '''View for 4thot application'''
    return render_page(request,'thot.html', "4 thot",'{"name": "my thoughts exactly!"}')


def read_json_doc():
    path = join(DOC_ROOT, 'thots.js')
    if exists(path):
         return open(path).read().decode(encoding='UTF-8')
    else:
        return ("Path NOT found "+path)


def write_json_doc(json):
    path = join(DOC_ROOT, 'thots.js')
    return open(path, 'w').write(json)


def get_thot(request):
    '''Get the JSON data for the thot application'''
    try:
        return HttpResponse(read_json_doc())
    except:
        return HttpResponse('Error on get')


@csrf_exempt
def put_thot(request):
    '''Put the JSON data for the thot application'''
    try:
        write_json_doc(request.body)
        return HttpResponse(json.dumps([{"name":"bill", "children": []}]))  #request.body)  #read_json_doc())
    except:
        return HttpResponse('Error on post.')


def budget(request):
    '''Check to see if the document exists'''
    return render_page(request, 'budget.html', 'Budget', 'text')


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


def redirect(request,title):
    '''Go to a specific page'''
    append_log (join(request.get_host(), title))
    return HttpResponseRedirect('/'+title) 


def render_page(request,template,title,text):
    '''Format the web page with content'''
    site = domain_title(request.get_host())
    content =  {
        #'document': domain_directory(request.get_host()) + '/' + site + '-' + title,
        'site_title': site, 
        'user': request.user, 
        'title': site + '-' + title, 
        'text': text
    }
    page = loader.get_template (template)
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


def doc(request,title):
    '''If the note is a directory or a file display it'''
    append_log (join(request.get_host(), title))
    path = join(DOC_ROOT, title)
    text = render_doc_html(path)
    return render_page(request, 'doc.html', title, text)


def home(request):
    '''Render the home view'''
    dir = domain_directory(request.get_host())
    if dir=='seamanslog':
        return random_select(request, 'seamanslog')
    return  redirect(request, dir+'/Index')

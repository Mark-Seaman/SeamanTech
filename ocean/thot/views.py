from django.http        import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template    import loader, Context
from os import system, environ, listdir
from os.path import join, exists, isdir, dirname, basename
from random import choice
from subprocess import Popen,PIPE

from django_project.settings import DOC_ROOT


def render_page(request,template,title,text):
    '''Format the web page with content'''
    site = '4 Thot'
    content =  {
        'site_title': site, 
        'user': request.user, 
        'title': site + '-' + title, 
        'text': text
    }
    page = loader.get_template (template)
    return HttpResponse(page.render(Context(content)))


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


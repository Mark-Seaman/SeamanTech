from random import choice
from os import listdir
from os.path import join

from django_project.settings import DOC_ROOT
from doc.views import render_page, redirect


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
    return '<h3>%s</h3>' % choice(open(path).read().split('\n'))


def bible(request):
    return render_page (request, 'bible', random_file('bible'))

def reflect(request):
    return render_page (request, 'reflection', random_line('reflection/Questions'))

def review(request):
    return random_select(request, 'teaching')

def prayers(request):
    return random_select(request, 'prayers')


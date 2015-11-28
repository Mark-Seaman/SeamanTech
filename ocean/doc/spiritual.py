from random import choice
from os import listdir
from os.path import join

from django_project.settings import DOC_ROOT
from doc.notes import render_page, redirect, random_select, random_file, random_line


def bible(request):
    text = random_file('spiritual/bible')
    return render_page (request, 'bible', text)

def reflect(request):
    text = random_line('spiritual/reflection/Questions')
    return render_page (request, 'reflection', text)

def review(request):
    return random_select(request, 'spiritual/teaching')

def prayers(request):
    return random_select(request, 'spiritual/prayers')


from django.shortcuts import render
from django.http import HttpResponse
from os import listdir


def index(request):
    #files = listdir('/home/django/django_project')
    files = listdir('/home/seaman/Projects/seamantech/ocean/')
    return HttpResponse("Hello, Mark! Welcome to the water.\n"+' ,'.join(files))

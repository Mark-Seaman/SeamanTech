#!/usr/bin/env python

from os import environ, listdir, remove, system,  walk
from os.path import join, exists
from random import choice
from sys import argv

from django_project.settings import DOC_ROOT


def asciidoc_add(topic):
    '''Create a new asciidoc.'''
    path = asciidoc_add_test(topic)
    system('e '+path)


def asciidoc_add_test(topic):
    '''Create a new asciidoc.'''
    if topic:
        path = asciidoc_path(topic)
        print("New asciidoc:"+path)
        if exists(path):
            print('File already exists: '+path)
            return path
        with open(path,'w') as f:
            f.write('# asciidoc: '+topic)
        return path
    else:
        print('Must add a topic')


def asciidoc_delete(topic):
    '''Delete the asciidoc.'''
    path = asciidoc_path(topic)
    print("Delete asciidoc: "+path)
    if exists(path):
        remove(path)
    else:
        print('File does not exist: '+path)


def asciidoc_edit(topic):
    '''Edit the content of a asciidoc.'''
    if not topic:
        print('No topic specified')
        return
    path = asciidoc_path(topic)
    print("Edit asciidoc:",path)
    if exists(path):
        system('e '+path)
    else:
        print('File does not exist: '+path)


def asciidoc_help():
    '''Show all the asciidoc asciidocs and their usage.'''
    print('''
    usage: cmd asciidoc [args]

    asciidoc:

        add     [file] -- Add a new asciidoc
        delete  [file] -- Delete a asciidoc
        edit    [file] -- Edit the asciidoc
        list    [file] -- List all asciidocs
        path    [file] -- Lookup the path for the file
        show    [file] -- Show a asciidoc
            ''')


def asciidoc_html(topic):
    '''Render asciidoc text as HTML.'''
    text = open(DOC_ROOT+'/Public/Leverage/'+topic+'.asc').read()
    lines = text.split('\n')
    lines = [ convert_line(line) for line in lines ]
    text = '\n'.join(lines)
    link = '<p><a href="StartReading">Table of Contents</a></p><br>'
    return link+text


def convert_line(line):
    return convert_paragraphs(convert_heading(line)) 


def convert_paragraphs(line):
    if not line or line.startswith('*'):
        return '<p></p>'+line
    return line
   

def convert_heading(line):
    x = line.replace('=','')
    if line.startswith('===='):
        return '<h4>'+x+'</h4>'
    elif line.startswith('==='):
        return '<h3>'+x+'</h3>'
    elif line.startswith('=='):
        return '<h2>'+x+'</h2>'
    elif line.startswith('='):
        return '<h1>'+x+'</h1>'
    return line


def asciidoc_enumerate():
    '''Generator to produce a list of all topics'''
    root_dir = asciidoc_path()
    for root, dirnames, filenames in walk(root_dir):
        for filename in filenames:
            yield join(root, filename).replace(root_dir+'/','')


def asciidoc_list(root_dir,topic=None):
    '''List the parts of the asciidoc source code.'''
    print("List the contents of this asciidoc")
    for root, dirnames, filenames in walk(root_dir):
        for filename in filenames:
            if topic:
                if not topic == filename:
                    continue
            print(join(root, filename).replace(root_dir+'/',''))


def asciidoc_path(topic=None):
    if topic:
        return join(environ['asciidoc'],topic)
    else:
        return environ['asciidoc']


def asciidoc_pick(topic):
    '''Select a topic to edit'''
    system('e '+asciidoc_path(choice(list(asciidoc_enumerate()))))


def asciidoc_show(topic):
    '''Show the content of a asciidoc.'''
    if topic:
        path = asciidoc_path(topic)
        print("Show asciidoc: "+path)
        if exists(path):
            print(open(path).read())
            return
        print('File does not exists: '+path)
    else:
        print('No topic listed')


def get_topic(argv):
    if len(argv)>2:
        return argv[2]
    

def asciidoc_command(argv):
    '''Execute all of the asciidoc specific asciidocs'''
    if len(argv)>1:

        if argv[1]=='add':
            asciidoc_add(get_topic(argv))

        elif argv[1]=='add_test':
            asciidoc_add_test(get_topic(argv))

        elif argv[1]=='delete':
            asciidoc_delete(get_topic(argv))

        elif argv[1]=='edit':
            asciidoc_edit(get_topic(argv))

        elif argv[1]=='list':
            asciidoc_list(asciidoc_path(), get_topic(argv))

        elif argv[1]=='path':
            print(asciidoc_path(get_topic(argv)))

        elif argv[1]=='pick':
            asciidoc_pick(get_topic(argv))

        elif argv[1]=='show':
            asciidoc_show(get_topic(argv))

        else:
            print('No asciidoc command found, '+argv[1])
            asciidoc_help()
    else:
        print('No arguments given')
        asciidoc_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
    asciidoc_command(argv)


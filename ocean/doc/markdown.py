#!/usr/bin/env python

from os import environ, listdir, remove, system,  walk
from os.path import exists, isdir, isfile, join
from random import choice
from re import sub
from sys import argv

from shell import print_banner, print_file, read_file
from util.wiki import muse_to_html


def markdown_add(topic):
    '''Create a new markdown.'''
    path = markdown_add_test(topic)
    system('e '+path)


def markdown_add_test(topic):
    '''Create a new markdown.'''
    if topic:
        path = markdown_path(topic)
        print("New markdown:"+path)
        if exists(path):
            print('File already exists: '+path)
            return path
        with open(path,'w') as f:
            f.write('# markdown: '+topic)
        return path
    else:
        print('Must add a topic')


def markdown_delete(topic):
    '''Delete the markdown.'''
    path = markdown_path(topic)
    print("Delete markdown: "+path)
    if exists(path):
        remove(path)
    else:
        print('File does not exist: '+path)


def markdown_edit(topic):
    '''Edit the content of a markdown.'''
    if not topic:
        print('No topic specified')
        return
    path = markdown_path(topic)
    print("Edit markdown:",path)
    if exists(path):
        system('e '+path)
    else:
        print('File does not exist: '+path)


def markdown_enumerate():
    '''Generator to produce a list of all topics'''
    root_dir = markdown_path()
    for root, dirnames, filenames in walk(root_dir):
        for filename in filenames:
            yield join(root, filename).replace(root_dir+'/','')


def markdown_help():
    '''Show all the markdown markdowns and their usage.'''
    print('''
    usage:  markdown cmd [args]

    cmd:

        add     [file] -- Add a new markdown
        delete  [file] -- Delete a markdown
        edit    [file] -- Edit the markdown
        html           -- Show the matching HTML
        list    [file] -- List all markdowns
        path    [file] -- Lookup the path for the file
        text    [file] -- Show markdown text
            ''')


def markdown_html(topic):
    ''' Edit the content of a command.'''
    path = markdown_path(topic)
    text = read_file(path)
    print(muse_to_html(text_to_muse(text)))


def markdown_list(root_dir,topic=None):
    '''List the parts of the markdown source code.'''
    print("List the contents of this markdown")
    for root, dirnames, filenames in walk(root_dir):
        for filename in filenames:
            if topic:
                if not topic == filename:
                    continue
            print(join(root, filename).replace(root_dir+'/',''))


def markdown_path(topic=None):
    path = environ['mybook']
    if topic:
        path = join(path,topic)
    return path


def markdown_pick(topic):
    '''Select a topic to edit'''
    system('e '+markdown_path(choice(list(markdown_enumerate()))))


def markdown_show(topic):
    ''' Show the content of a doc.'''
    path = markdown_path(topic)
    if isdir(path):
        for f in markdown_enumerate():
            if isfile(join(path,f)):
                print_banner (f)
                print_file(join(path,f))
    elif isfile(path):
        print_file(path)


def get_topic(argv):
    if len(argv)>2:
        return argv[2]
    

# Convert a text block
def text_to_markdown(text):
    '''Convert Muse text to markdown'''

    def map_muse_to_markdown(line):
        line = sub(r'^\* ', r'# ', line)
        line = sub(r'^\*\* ', r'## ', line)
        line = sub(r'^\s*\* ', r'* ', line)
        line = sub(r'\[\[(LinkText)\]\]', r'\[\[\2\]\]', line)
        return line

    text = map(map_muse_to_markdown, text.split('\n'))
    return '\n'.join(text)


# Convert a text block
def text_to_muse(text):
    '''Convert markdown text to Muse'''

    # Apply a stack of substitutions
    def map_markdown_to_muse(line):
        line = sub(r'^\* ', r' * ', line)
        line = sub(r'\*\*', r'**', line)
        line = sub(r'^# ',  '* ', line)
        line = sub(r'^## ', '** ', line)
        line = sub(r'^### ', '*** ', line)
        line = sub(r'^#### ', '**** ', line)
        line = sub(r'\[(.*)\]\((.*)\)', r'[[\1][\2]]',line)
        return line

    text = map(map_markdown_to_muse, text.split('\n'))
    return '\n'.join(text)


def markdown_command(argv):
    '''Execute all of the markdown specific markdowns'''
    if len(argv)>1:

        if argv[1]=='add':
            markdown_add(get_topic(argv))

        elif argv[1]=='add_test':
            markdown_add_test(get_topic(argv))

        elif argv[1]=='delete':
            markdown_delete(get_topic(argv))

        elif argv[1]=='edit':
            markdown_edit(get_topic(argv))

        elif argv[1]=='html':
			markdown_html(argv[2])

        elif argv[1]=='list':
            markdown_list(markdown_path(), get_topic(argv))

        elif argv[1]=='path':
            print(markdown_path(get_topic(argv)))

        elif argv[1]=='pick':
            markdown_pick(get_topic(argv))

        elif argv[1]=='text':
            markdown_show(get_topic(argv))

        else:
            print('No markdown command found, '+argv[1])
            markdown_help()
    else:
        print('No arguments given')
        markdown_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
    markdown_command(argv)

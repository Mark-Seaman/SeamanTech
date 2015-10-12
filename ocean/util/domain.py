
from datetime   import datetime
from os         import system
from os.path    import isfile, exists,join
from re         import compile, IGNORECASE, DOTALL

from wiki  import *
from tabs  import format_tabs, format_doc
from files import read_input, read_text, write_file, is_writable
from django_project.settings import DOC_ROOT


domain_info = {
    'world-class-software.com': { 
        'directory': 'Leverage', 
        'title': 'The Leverage Principle'
    },
    'spiritual-things.org': { 
        'directory': 'Spiritual-Things.org', 
        'title': 'Quiet Moments'
    },
    'seamanslog.com': {
        'directory': 'SeamansLog.com',
        'title': "Seaman's Log"
    },
    'mybookonline.org': {
        'directory': 'mybookonline.org',
        'title': 'mybookonline.org'
    },
    'exteriorbrain.com': {
        'directory': 'Brain',
        'title': 'Exterior Brain'
    },
    'seaman-tech.com': {
        'directory': 'seaman-tech.com',
        'title': 'Seaman Tech'
    },
    'markseaman.info': {
        'directory': 'MarkSeaman.info',
        'title': 'Mark Seaman.info'
    },
    'markseaman.org': {
        'directory': 'MarkSeaman.org',
        'title': 'Markos de Seaman'
    }
}

# Read the domain mapping from a file
def domain_title(domain):
    if domain_info.has_key(domain):
        return domain_info[domain]['title']
    else:
        return 'Local Host'


# Map the domain to a document directory
def domain_directory(domain):
    if domain_info.has_key(domain):
        return domain_info[domain]['directory']
    else:
        return ''


# Convert a url to a directory
def doc_path(path):
    dir = domain_directory(path[0])
    if not dir: 
        dir = '.'
    if len(path)>1:
        user = path[1].replace('Anonymous', 'Public')
    else:
        user = 'Public'
    return '/'.join( [user,dir] + path[2:] )


# Convert a url to a directory
def public_doc_path(path):
    path = doc_path(path.split('/'))
    path[1] = 'Public'
    return doc_path(path)


# Return the new url to visit  (Implied path host/user/doc)
def redirect_path(doc):
    path = doc.split('/')
    url = '/'.join(path[2:])
    return url


# lookup the path for the doc for this url
def map_doc_path(url):
    doc = doc_path(url.split('/'))
    return join(DOC_ROOT, doc)


# Either format the doc or return the redirect page
def doc_redirect (url):
    doc = map_doc_path(url)
    if exists(doc):
        if not isfile(doc):
            index = join(doc,'Index')
            if exists(index):
                return redirect_path(url) + '/Index'
            else:
                return redirect_path(url) + '/Index/missing'
    else:
        return redirect_path(url) + '/missing' 


# Either format the doc or return the redirect page
def show_domain_doc(url):
    doc = map_doc_path(url)
    if exists(doc) and isfile(doc):
        text = read_text(doc)
        return format_tabs(text)


# Put the document text in storage
def put_domain_doc(doc):
    write_file(map_doc_path(doc), read_input())


# Get the document text from storage
def get_domain_doc(doc):
    if not doc_redirect(doc):
        print read_text(map_doc_path(doc))
    else:
        print "redirect:%s/missing" % doc_redirect(doc)


#  Formatter to add tabs to the HTML formatting
def print_tab_doc(filename):
    print format_doc(filename)


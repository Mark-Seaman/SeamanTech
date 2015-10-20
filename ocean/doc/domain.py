# Table of domain info for websites

domain_info = {
    'world-class-software.com': { 
        'directory': 'Leverage', 
        'title': 'The Leverage Principle'
    },
    'spiritual-things.org': { 
        'directory': 'spiritual', 
        'title': 'Quiet Moments'
    },
    'seamanslog.com': {
        'directory': 'seamanslog',
        'title': "Seaman's Log"
    },
    'mybookonline.org': {
        'directory': 'mybook',
        'title': 'mybookonline.org'
    },
    'exteriorbrain.com': {
        'directory': 'brain',
        'title': 'Exterior Brain'
    },
    'seaman-tech.com': {
        'directory': 'tech',
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




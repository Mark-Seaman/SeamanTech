# Test the storage of Key-Value pairs

from re import sub
from markdown import text_to_muse, text_to_markdown


# Muse, markdown pairs
test_cases = [

    ( '',  ''),

    ( 'This is a **test** for text', 'This is a **test** for text'),

    ( ' * This is a **test** for text',  '* This is a **test** for text'),

    ( 'link [[LinkText]]', 'link [[LinkText]]'),

]


# Compare two strings
def same (s1,s2):
    if s1!=s2:
        print 'Mismatch:%s|%s|'%(s1,s2)
        assert(False) 


# Convert muse text to markdown
def to_markdown_test():
    for t in test_cases:
        same (text_to_markdown(t[0]), t[1])


# Convert muse text to markdown
def from_markdown_test():
    for t in test_cases:
        same (text_to_muse(t[1]), t[0])


# Try to substitute text with a REGEX
def substitute_test():
    t = ( 'link [[LinkText][linking text]] more text', 'link [LinkText](linking text) more text' )

    markdown_link = r'\[([\w ]+)\]\(([\w ]+)\)'
    markdown_subs = r'[[\1][\2]]'
    same (sub(markdown_link,markdown_subs,t[1]), t[0])

    muse_link = r'\[\[([\w ]+)\]\[([\w ]+)\]\]'
    muse_subs = r'[\1](\2)'
    same (sub(muse_link, muse_subs,t[0]), t[1])

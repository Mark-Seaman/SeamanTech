# Test the storage of Key-Value pairs

from re import sub
from markdown import text_to_muse, text_to_markdown, replacer


# Text replacement patterns

muse_text     = 'link [[LinkText][linking text]] more text'
muse_link     = r'\[\[([\w ]+)\]\[([\w ]+)\]\]'
muse_subs     = r'[\2](\1)'

markdown_text = 'link [linking text](LinkText) more text'
markdown_link = r'\[([\w ]+)\]\(([\w ]+)\)'
markdown_subs = r'[[\2][\1]]'

muse_repl     = (muse_link,muse_subs)
markdown_repl = (markdown_link,markdown_subs)


# Muse, markdown pairs (muse, markdown)
test_cases = [

    ( '',  ''),

    ( 'This is a **test** for text', 'This is a **test** for text'),

    ( ' * This is a **test** for text',  '* This is a **test** for text'),

    ( 'link [[LinkText]]', 'link [[LinkText]]'),

    ('link [[LinkText][linking text]] more text', 
     'link [linking text](LinkText) more text' ),

    ( '''
* Muse/Markdown Text Pattern 
 * Bullet point
** Subtopic
This is **bold** text
    indented text

[[LinkTopic]]
Text [[RandomTopic][this random topic]] other text on line.

      ''', 
      '''
# Muse/Markdown Text Pattern 
* Bullet point
## Subtopic
This is **bold** text
    indented text

[[LinkTopic]]
Text [this random topic](RandomTopic) other text on line.

      '''),
]


# Compare two strings
def same (s1,s2):
    if s1!=s2:
        print 'Mismatch:|%s|%s|'%(s1,s2)
        assert(False) 


# Try to substitute text with a REGEX
def substitute_test():
    same (sub(markdown_link, markdown_subs, markdown_text), muse_text)
    same (sub(muse_link, muse_subs, muse_text), markdown_text)

 
# Convert a line to muse and back to markdown using the same replacer   
def round_trip_test():
    replacements = (muse_repl,markdown_repl)
    assert (replacer(replacements,muse_text) == muse_text)
    assert (replacer(replacements,markdown_text) != markdown_text)


# Replacement tester
def to_muse_test():
    for t in test_cases:
        same (text_to_muse(t[1]), t[0])


# Convert muse text to markdown
def to_markdown_test():
    for t in test_cases:
        same (text_to_markdown(t[0]), t[1])


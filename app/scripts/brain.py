#!/usr/bin/env python
# Brain commands

from sys import argv

from doc.doc_query import print_doc_list, import_doc, show_doc, reset_doc_list,search

def run():
    #print 'argv: ',argv

    if len(argv)<4:
        print 'usage: rs brain command parm'
        exit(0)


    if argv[3].startswith('list'):
        expr = 'list('+','.join(argv[4:])+')'
        print  expr
        search(argv[4:])
        #print_doc_list(title='Plan', content='Market')
        exit(0)


    if argv[3]=='show':
        if len(argv)<5:
            print 'usage: rs brain show doc'
        else:
            show_doc('seaman', argv[4])
        exit(0)


    if argv[3]=='clear':
        if len(argv)<5:
            print 'usage: rs brain clear doc'
        else:
            reset_doc_list('seaman', argv[4])
        exit(0)
        

    if argv[3]=='import':
        if len(argv)<5:
            print 'usage: rs brain import file'
        else:
            import_doc(argv[4])
        exit(0)

    print 'usage: rs brain command parm\ncommand = [list]'
    exit(0)


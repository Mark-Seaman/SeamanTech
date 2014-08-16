# Doc commands

from sys import argv

from doc.doc_query import print_list, reset_list, test_doc, count


def run():
    #print 'argv: ',argv

    if len(argv)<4:
        print 'usage: rs doc command parm'
        exit(0)


    if argv[3]=='list':
        print_list()
        exit(0)


    if argv[3]=='count':
        print '%d Doc records'%count()
        exit(0)


    if argv[3]=='test':
        test_doc()
        exit(0)


    if argv[3]=='clear':
        reset_list()
        exit(0)
        

    print 'usage: rs doc command parm\ncommand = [list]'
    exit(0)


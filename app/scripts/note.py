# Note commands

from sys import argv

from note.note_query import print_list, reset_list, test_note, count


def run():
    #print 'argv: ',argv

    if len(argv)<4:
        print 'usage: rs note command parm'
        exit(0)


    if argv[3]=='list':
        print_list()
        exit(0)


    if argv[3]=='count':
        print '%d Note records'%count()
        exit(0)


    if argv[3]=='test':
        test_note()
        exit(0)


    if argv[3]=='clear':
        reset_list()
        exit(0)
        

    print 'usage: rs note command parm\ncommand = [list]'
    exit(0)


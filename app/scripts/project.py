# Project commands

from sys import argv

from task.project_query import print_list, reset_list, test_project, count


def run():
    #print 'argv: ',argv

    if len(argv)<4:
        print 'usage: rs project command parm'
        exit(0)


    if argv[3]=='list':
        print_list()
        exit(0)


    if argv[3]=='count':
        print '%d Project records'%count()
        exit(0)


    if argv[3]=='test':
        test_project()
        exit(0)


    if argv[3]=='clear':
        reset_list()
        exit(0)
        

    print 'usage: rs project command parm\ncommand = [list]'
    exit(0)


# Time commands

from sys import argv

from task.time_query import print_list, reset_list, test_time, count


def run():
    #print 'argv: ',argv

    if len(argv)<4:
        print 'usage: rs time command parm'
        exit(0)


    if argv[3]=='list':
        print_list()
        exit(0)


    if argv[3]=='count':
        print '%d Time records'%count()
        exit(0)


    if argv[3]=='test':
        test_time()
        exit(0)


    if argv[3]=='clear':
        reset_list()
        exit(0)
        

    print 'usage: rs time command parm\ncommand = [list]'
    exit(0)


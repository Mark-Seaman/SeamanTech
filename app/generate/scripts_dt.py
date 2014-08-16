# Data_Type commands

from sys import argv

from module_name.data_type_query import print_list, reset_list, test_data_type, count


def run():
    #print 'argv: ',argv

    if len(argv)<4:
        print 'usage: rs data_type command parm'
        exit(0)


    if argv[3]=='list':
        print_list()
        exit(0)


    if argv[3]=='count':
        print '%d Data_Type records'%count()
        exit(0)


    if argv[3]=='test':
        test_data_type()
        exit(0)


    if argv[3]=='clear':
        reset_list()
        exit(0)
        

    print 'usage: rs data_type command parm\ncommand = [list]'
    exit(0)


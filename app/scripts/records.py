# Count the database records

#from doc.doc_model   import Doc
#from task.time_model import Time

def count_records(object,label):
    print len(object.objects.all()),label

def run():
#    count_records(Doc,'Doc')
#    count_records(Time,'Time')
    print 'No records listed'



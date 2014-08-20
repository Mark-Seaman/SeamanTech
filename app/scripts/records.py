# Count the database records

from task.time_model    import Time
from task.project_model import Project

def count_records(object,label):
    print len(object.objects.all()),label

def run():
    count_records(Project,'Project')
    count_records(Time,'Time')
    #print 'No records listed'



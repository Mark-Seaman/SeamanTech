# task/time_query.py
# Model for Time records

from django.contrib.auth.models import User
from random        import choice,randint

from project_model import Project
from time_model    import Time
from faker         import fake_task


# Get a table listing from the database
def select_time(user=None):
    if user:
        return Time.objects.filter(user=user)
    else:
        return Time.objects.all()
    return [ f.values() for f in objects ]


# Get a table listing from the database
def query_time(user=None):
    return [ f.values() for f in select_time(user) ]


# Return a single contact
def get_time(user,id):
    a =  Time.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Count the saved Time records
def count():
    return len(Time.objects.all())


# Print the object fields as a table
def print_time(time):
    for x in time.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Print the object list as a table
def print_list():
    all = Time.objects.all()
    print 'Time list:  %d records' % len(all)
    for c in all:
        print_time(c)


# Remove the all times from the database
def reset_list():
    Time.objects.all().delete()


# Add a new record from a file
def add_time(data):
    o =  Time.objects.filter(name=data[0])
    if len(o)==1:
        c = o[0]
    else:
        c = Time()
    c.user,c.project,c.name, c.task,c.minutes = data
    c.save()
    return c

# Select a random user
def random_user():
    return choice(User.objects.all())
# Select a random project

def random_project():
    return choice(Project.objects.all())


# Add some fake Time records
def add_fake_time(num=1):
    for i in range(num):
        data = [random_user(), random_project(), fake_task(), fake_task(),randint(30,90)]
        add_time(data)


# Test Time code
def test_time():
    if count()<10:
        add_fake_time(1)



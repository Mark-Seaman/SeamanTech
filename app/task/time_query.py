# task/time.py
# Model for Time records

from django.contrib.auth.models import User

from time_model import Time
from doc.faker import fake_name,fake_address,fake_phone_number,fake_company


# Get a table listing from the database
def query_time(user=None):
    if user:
        objects = Time.objects.filter(user=user)
    else:
        objects = Time.objects.all()
    return [ f.values() for f in objects ]


# Return a single contact
def get_time(user,id):
    a =  Time.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Print the object fields as a table
def print_time(time):
    for x in time.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Print the object list as a table
def print_time_list():
    all = Time.objects.all()
    print 'Time list:  %d records' % len(all)
    for c in all:
        print_time(c)


# Generate a new record if needed
def add_fake_time():
    c = Time()
    c.user = User.objects.get(username='TestRobot')
    c.name = fake_name()
    c.task = fake_address()
    c.save()
    return c


# Remove the all times from the database
def reset_time_list():
    Time.objects.all().delete()


# Perform a test on time. If there are no times then make some.
def test_code():
    if len(Time.objects.all())<1:
        how_many = 4
        for c in range(how_many):
            add_fake_time()
    print_time_list()
    


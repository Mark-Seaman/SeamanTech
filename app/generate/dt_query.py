# module_name/data_type_query.py
# Model for Data_Type records

#from django.contrib.auth.models import User

from data_type_model import Data_Type

from faker import fake_name


# Get a table listing from the database
def select_data_type(user=None):
    if user:
        return Data_Type.objects.filter(user=user)
    else:
        return Data_Type.objects.all()
    return [ f.values() for f in objects ]


# Get a table listing from the database
def query_data_type(user=None):
    return [ f.values() for f in select_data_type(user) ]


# Return a single contact
def get_data_type(user,id):
    a =  Data_Type.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Count the saved Data_Type records
def count():
    return len(Data_Type.objects.all())


# Print the object fields as a table
def print_data_type(data_type):
    for x in data_type.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Print the object list as a table
def print_list():
    all = Data_Type.objects.all()
    print 'Data_Type list:  %d records' % len(all)
    for c in all:
        print_data_type(c)


# Remove the all data_types from the database
def reset_list():
    Data_Type.objects.all().delete()


# Add a new record from a file
def add_data_type(data):
    o =  Data_Type.objects.filter(name=data[0])
    if len(o)==1:
        c = o[0]
    else:
        c = Data_Type()
    #c.name, c.address, c.phone = data
    c.save()
    return c


# Add some fake Data_Type records
def add_fake_data_type(num=1):
    for i in range(num):
        data = [fake_name()]
        add_data_type(data)


# Test Data_Type code
def test_data_type():
    if count()<10:
        add_fake_data_type(1)



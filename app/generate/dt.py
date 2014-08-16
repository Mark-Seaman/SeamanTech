# srs/data_type.py
# Model for Data_Type records

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

    
# Define a contact data type
class Data_Type(models.Model):
    name    = models.CharField (max_length=40)
    user    = models.ForeignKey(User)


    # Format a record as a string
    def __unicode__(self):
        return self.name

    # Back trace a url to a view
    def get_absolute_url(self):
        return reverse('data_type-detail', kwargs={'pk': self.pk})

    # Object field handling
    def __iter__(self):
        for i in self.fields():
            yield (i, getattr(self, i))

    # Enumerate the fields
    def fields(self):
        return [ f.name for f in self._meta.fields ]

    # List of values
    def values(self):
        return [ v for f,v in self ]

    # Table of field labels and values
    def table(self):
        return zip(self.fields(),self.values())

#---------------------------------------------------------

# Get a table listing from the database
def query_data_type(user=None):
    if user:
        objects = Data_Type.objects.filter(user=user)
    else:
        objects = Data_Type.objects.all()
    return [ f.values() for f in objects ]


# Return a single contact
def get_data_type(user,id):
    a =  Data_Type.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Print a data_type as a table of fields
def print_data_type(data_type):
    for x in data_type.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Show the object in several different forms
def show_data_type(data_type):
    print 'Data_Type:', data_type.name
    print 'Fields:', data_type.fields()
    print 'Values:', data_type.values()
    print 'Table:', data_type.table()
    print_data_type(data_type)


# Generate a new record if needed
def add_fake_data_type(name):
    print 'Make data_type: ', name
    c = Data_Type()
    #c.user = User.objects.get(name='TestRobot')
    #c.name = name
    #c.address = 'Here'
    #c.phone = '900-555-1212'
    c.save()
    return c


# Perform a test on this object type
def test_code():

    # Count current records
    num_data_types = len(query_data_type())
    print '%d Data_Types' % num_data_types

    # Delete all records
    #Data_Type.objects.all().delete()

    # If there are no data_types then make some
    if num_data_types<1:
        fake_names = [ 'Tom', 'Jerry', 'Billy', 'Bob' ]
        for c in fake_names:
            add_fake_data_type(c)

    # Print a list of all names
    all = Data_Type.objects.all()
    print 'Data_Type list:  %d records' % len(all)
    for c in all:
        print_data_type(c)


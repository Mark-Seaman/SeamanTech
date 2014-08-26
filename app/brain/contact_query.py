# brain/contact.py
# Model for Contact records

from django.contrib.auth.models import User

from contact_model import Contact


# Get a table listing from the database
def query_contact(user=None):
    if user:
        objects = Contact.objects.filter(user=user)
    else:
        objects = Contact.objects.all()
    return [ f.values() for f in objects ]


# Return a single contact
def get_contact(user,id):
    a =  Contact.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Generate a new record if needed
def add_fake_contact(name):
    print 'Make contact: ', name
    c = Contact()
    #c.user = User.objects.get(name='TestRobot')
    #c.name = name
    #c.address = 'Here'
    #c.phone = '900-555-1212'
    c.save()
    return c


# Perform a test on this object type
def test_code():

    # Count current records
    num_contacts = len(query_contact())
    print '%d Contacts' % num_contacts

    # Delete all records
    #Contact.objects.all().delete()

    # If there are no contacts then make some
    if num_contacts<1:
        fake_names = [ 'Tom', 'Jerry', 'Billy', 'Bob' ]
        for c in fake_names:
            add_fake_contact(c)

    # Print a list of all names
    all = Contact.objects.all()
    print 'Contact list:  %d records' % len(all)
    for c in all:
        print_contact(c)


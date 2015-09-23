# note/note_query.py
# Model for Note records

#from django.contrib.auth.models import User

from note_model import Note

from faker import fake_name


# Get a table listing from the database
def select_note(user=None):
    if user:
        return Note.objects.filter(user=user)
    else:
        return Note.objects.all()
    return [ f.values() for f in objects ]


# Get a table listing from the database
def query_note(user=None):
    return [ f.values() for f in select_note(user) ]


# Return a single contact
def get_note(user,id):
    a =  Note.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Count the saved Note records
def count():
    return len(Note.objects.all())


# Print the object fields as a table
def print_note(note):
    for x in note.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Print the object list as a table
def print_list():
    all = Note.objects.all()
    print 'Note list:  %d records' % len(all)
    for c in all:
        print_note(c)


# Remove the all notes from the database
def reset_list():
    Note.objects.all().delete()


# Add a new record from a file
def add_note(data):
    o =  Note.objects.filter(name=data[0])
    if len(o)==1:
        c = o[0]
    else:
        c = Note()
    #c.name, c.address, c.phone = data
    c.save()
    return c


# Add some fake Note records
def add_fake_note(num=1):
    for i in range(num):
        data = [fake_name()]
        add_note(data)


# Test Note code
def test_note():
    if count()<10:
        add_fake_note(1)



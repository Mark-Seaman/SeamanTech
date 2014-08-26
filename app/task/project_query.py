# task/project_query.py
# Model for Project records


from project_model import Project

from faker import fake_project, fake_task, fake_company


# Get a table listing from the database
def select_project(user=None):
    if user:
        return Project.objects.filter(user=user)
    else:
        return Project.objects.all()
    return [ f.values() for f in objects ]


# Get a table listing from the database
def query_project(user=None):
    return [ f.values() for f in select_project(user) ]


# Return a single contact
def get_project(user,id):
    a =  Project.objects.filter(pk=id)
    if len(a)==1:
        return a[0].table()


# Count the saved Project records
def count():
    return len(Project.objects.all())


# Print the object fields as a table
def print_project(project):
    for x in project.table():
        print '    %-10s:  %s' % (x[0],x[1])
    print


# Print the object list as a table
def print_list():
    all = Project.objects.all()
    print 'Project list:  %d records' % len(all)
    for c in all:
        print_project(c)


# Remove the all projects from the database
def reset_list():
    Project.objects.all().delete()


# Add a new record from a file
def add_project(data):
    o =  Project.objects.filter(name=data[0])
    if len(o)==1:
        c = o[0]
    else:
        c = Project()
    c.name, c.client,c.task = data
    c.save()
    return c


# Add some fake Project records
def add_fake_project(num=1):
    for i in range(num):
        data = [fake_project(),fake_company(),fake_task()]
        add_project(data)


# Test Project code
def test_project():
    if count()<10:
        add_fake_project(1)



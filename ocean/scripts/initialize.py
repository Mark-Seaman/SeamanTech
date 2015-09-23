# Initialize the required users in the system

from django.contrib.auth.models import User


# Make sure there is one Super User
def check_super_user():
    if len(User.objects.filter(username='SuperUser'))!=1:
        print 'Bad super user config'
    else:
        print '   Super user - OK'

# Make sure there is one Test Robot user
def check_test_robot():
    if len(User.objects.filter(username='TestRobot'))!=1:
        print 'Create TestRobot user'
        name = 'TestRobot'
        email = 'mark.b.seaman+TestRobot@gmail.com'
        pw =  'x'
        user = User.objects.create_user(name, email, pw)
    if len(User.objects.filter(username='TestRobot'))==1:
        print '   Test Robot - OK'


# Make sure there is one Test Robot user
def check_seaman():
    users = User.objects.filter(username='seaman')
    if len(users)!=1:
        print 'Create seaman user'
        name = 'seaman'
        email = 'mark.b.seaman+SeamanTech@gmail.com'
        pw =  'MS2014st'
        user = User.objects.create_user(name, email, pw)
    if len(users)==1:
        users[0].is_staff = True
        users[0].save()
        print '   seaman - OK'


# Check that the correct users are set up
def run():
    print 'Checking for users:'
    check_super_user()
    check_test_robot()
    check_seaman()

# Test all data types

from os import system

from srs.provider_query  import add_fake_provider
from srs.company_query   import add_fake_company
from srs.employee_query  import add_fake_employee
from srs.topic_query     import add_fake_topic
from srs.topicflags_query import add_fake_topicflags
from srs.topicbehavior_query import add_fake_topicbehavior
from srs.comment_query   import add_fake_comment


# Run the main job
def run():
    print 'Records before test'
    system('rs records')

    for i in range(10):
        add_test_data()

    print '\nRecords after test'
    system('rs records')


# Create random employees and companies
def add_test_data():
    print 'add_test_data'    
    add_fake_provider ()
    add_fake_company ()
    add_fake_employee ()
    add_fake_topic ()
    add_fake_topicflags ()
    add_fake_topicbehavior ()
    add_fake_comment ()

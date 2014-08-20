# Test all data types

from os import system

from task.time_query    import test_time
from task.project_query import test_project
#from note.note_query    import test_note


# Run the main job
def run():

    test_time()
    test_project()
    #test_note()

    system ('rs records')

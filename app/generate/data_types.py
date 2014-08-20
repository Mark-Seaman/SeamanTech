# Data types to create for this application

data_types = {

   #-----------------------------------------------------------------------------

    'Note': {
        'module': 'note',
        'class': 
'''
from datetime import datetime

class Note(models.Model):

    user    = models.ForeignKey(User)
    path    = models.CharField (max_length=200)
    title   = models.CharField (max_length=200)
    text    = models.TextField ()
    time    = models.DateTimeField(auto_now_add=True)  
'''

    },

    #-----------------------------------------------------------------------------

    'Project': {
        'module': 'task',
        'class': 
'''
class Project(models.Model):

    name    = models.CharField (max_length=40)
    client  = models.CharField (max_length=40)
    task    = models.CharField (max_length=40)
    date    = models.DateField (auto_now_add=True)  
    notes   = models.TextField (null=True)
'''

    },

    #-----------------------------------------------------------------------------

    'Time': {
        'module': 'task',
        'class': 
'''
class Time(models.Model):

    user    = models.ForeignKey (User)
    project = models.ForeignKey (Project)
    name    = models.CharField  (max_length=40)
    task    = models.CharField  (max_length=40)
    date    = models.DateField  (auto_now_add=True)  
    minutes = models.IntegerField(default='60')
'''

    },   

}

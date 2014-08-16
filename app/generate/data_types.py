# Data types to create for this application

data_types = {

   #-----------------------------------------------------------------------------

    'Doc': {
        'module': 'doc',
        'class': 
'''
from datetime import datetime

class Doc(models.Model):

    user    = models.ForeignKey(User)
    path    = models.CharField (max_length=200)
    title   = models.CharField (max_length=200)
    text    = models.TextField ()
    time    = models.DateTimeField(default= datetime.now())  
'''

    },

    #-----------------------------------------------------------------------------

    'Time': {
        'module': 'task',
        'class': 
'''
class Time(models.Model):

    user    = models.ForeignKey(User)
    name    = models.CharField (max_length=200)
    task    = models.CharField (max_length=40)
    date    = models.DateField(auto_now_add=True)  
    minutes = models.IntegerField(default='60')
'''

    },

}

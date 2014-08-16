"""
Test all of the event catering code
"""

from django.test import TestCase
from note import *

class NoteTest(TestCase):

    def test_note(self):
        """
        Test the note data type
        """

        # Setup test records with 10 new records
        test_note()
        self.assertEqual(10,len(Note.objects.filter(name__startswith='Name ')))
        self.assertEqual(10,len(Note.objects.all()))

        # Convert to string 
        a = note_get(3)
        s = note_detail(a)
        answer = [3, u'Name 3', u'Note 3', u'', u'City 3', u'State 3', u'Zip 3', u'Phone 3',
                  0.0, u'Email 3', u'']
        self.assertEqual(s,answer)

        # Show the labels for a table
        s = note_labels
        answer =  [ 'id', 'name', 'note1', 'note2', 'city', 'state', 'zipcode', 'phone', 
                    'tax_rate', 'email', 'notes',]
        self.assertEqual(s,answer)

        # Show the list for the details 
        s = notees()
        answer =  [[1, u'Name 1', u'Phone 1'], [2, u'Name 2', u'Phone 2'], 
                   [3, u'Name 3', u'Phone 3'], [4, u'Name 4', u'Phone 4'], 
                   [5, u'Name 5', u'Phone 5'], [6, u'Name 6', u'Phone 6'], 
                   [7, u'Name 7', u'Phone 7'], [8, u'Name 8', u'Phone 8'], 
                   [9, u'Name 9', u'Phone 9'], [10, u'Name 10', u'Phone 10']]
        self.assertEqual(s,answer)


from django.db import models


class Thot (models.Model):
    name     = models.CharField (max_length=100)
    text     = models.TextField (null=True)
    parent   = models.ForeignKey('self', null=True) 


def add_thot(name):
    t = Thot()
    t.name = name
    t.save()


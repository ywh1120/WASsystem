from __future__ import unicode_literals

from django.db import models

def generate_filename(self, filename):
    url = '/'.join(['content',self.title, filename])
    return url

class Graph(models.Model):
    title = models.CharField(max_length=200)
    jan_data = models.IntegerField()
    feb_data = models.IntegerField()
    mar_data = models.IntegerField()
    apr_data = models.IntegerField()
    may_data = models.IntegerField()
    jun_data = models.IntegerField()
    jul_data = models.IntegerField()
    aug_data = models.IntegerField()
    sep_data = models.IntegerField()
    oct_data = models.IntegerField()
    nov_data = models.IntegerField()
    dec_data = models.IntegerField()
    yaxis_val = models.IntegerField()
    
class Pdfdata(models.Model):
    title = models.CharField(max_length=300)
    pdffile = models.FileField(upload_to=generate_filename,null='true')
    
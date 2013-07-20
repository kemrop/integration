from django.db import models

# Create your models here.

import urllib2

class GoodReadsApi:
    #response = urllib2.urlopen('http://www.google.com')
    response = urllib2.urlopen('http://www.goodreads.com/shelf/list.xml?user_id=2199404&key=AsjqixhpP69xo5aJkPlgw')
    html = response.read()





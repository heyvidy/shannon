from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import datetime

#For processing Avatars in User Profiles -- Django-Imagekit
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

#STDIMAGE
from stdimage.models import StdImageField

import os
from uuid import uuid4

YEAR_CHOICES = [(r,r) for r in range(1990, datetime.date.today().year+1)]

class Profile(models.Model):
    def __unicode__(self):
       return 'Profile: ' + self.profile_owner.first_name
    profile_owner = models.ForeignKey(User)
    USN = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    tenth_perc = models.DecimalField(max_digits=5, decimal_places = 3)
    tenth_yop = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    tenth_Board = models.CharField(max_length=100)
    twelth_perc = models.DecimalField(max_digits=5, decimal_places = 3)
    twelth_board = models.CharField(max_length=100)
    twelth_yop = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    eng_branch = models.CharField(max_length=100)
    # creates a thumbnail resized to 100x100 croping if necessary
    image = StdImageField(upload_to='photos/', variations={
        'thumbnail': {"width": 100, "height": 100, "crop": True}})

class Post(models.Model):
    def __unicode__(self):
       return self.post_title
    post_title = models.CharField(max_length = 150)
    post_body = models.TextField()
    post_time = models.DateTimeField()
    author = models.ForeignKey(User)

class Notice(models.Model):
    def __unicode__(self):
       return self.notice
    notice = models.CharField(max_length = 200)
    notice_description = models.CharField(max_length = 200)

class Document(models.Model):
    def __unicode__(self):
       return self.name

    name = models.CharField(max_length=200, default='')
    docfile = models.FileField(upload_to='files/')

    # For Tagging Files to respective subjects
    Labels = (
    ('dc', 'Digital Communications'),
    ('mec', 'Micro Electronic Circuits'),
    ('sc', 'Sat Comm'),
    ('mp', 'Micro Processors'),
    ('ap', 'Antenna & Propogation'),
    ('os', 'Operating Systems'),
)
    label = models.CharField(max_length=10, choices=Labels)

class Activity(models.Model):

    def __unicode__(self):
       return self.activity_name

    activity_name = models.CharField(max_length=100)
    activity_date = models.DateField()





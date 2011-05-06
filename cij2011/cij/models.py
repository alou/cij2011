#!/usr/bin/env python
# encoding=utf-8
# maintainer: alou

import datetime
from django.db import models


class Club(models.Model):
    """ Info of Club """
    name = models.CharField(max_length=30, verbose_name=("Name"))
    date_of_charter = models.DateField(verbose_name=("Date of charter"),\
                             default=datetime.datetime.today)
    godson = models.CharField(max_length=30, verbose_name=("Godson"))
    advisor = models.CharField(max_length=60, verbose_name=("Advisor"))
    president = models.CharField(max_length=60, verbose_name=("President"))
    secretary = models.CharField(max_length=60, verbose_name=("Secretary"))
    treasurer = models.CharField(max_length=60, verbose_name=("Treasurer"))
    director_of_Staff = models.CharField(max_length=60, verbose_name=("Director of Staff"))
    protocol = models.CharField(max_length=60, verbose_name=("Protocol"))
    seat = models.CharField(max_length=60, verbose_name=("Seat"))
    def __unicode__(self):
        return u'%(name)s' % {"name": self.name}
        

class Pamper(models.Model):
    """ Camper registered
    """
    first_name = models.CharField(max_length=30, verbose_name=("First Name"))
    last_name = models.CharField(max_length=30, verbose_name=("Last Name"))
    nationality = models.CharField(max_length=30, verbose_name=("Nationality"))
    adress = models.TextField(verbose_name=("Adress"))
    email = models.EmailField(blank=True, verbose_name=("Email"))
    date_to_arrive = models.DateField(verbose_name=("Date to arrive"),\
                             default=datetime.datetime.today)
    departure_date = models.DateField(verbose_name=("Departure date"),\
                             default=datetime.datetime.today)
    club = models.ForeignKey(Club, verbose_name=("Club"))
    def __unicode__(self):
        return u'%(first_name)s %(last_name)s ' % {"first_name": self.first_name,
                                                   "last_name": self.last_name}
# Create your models here

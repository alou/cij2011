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


class Country(models.Model):
    """ Info of country """
    name = models.CharField(max_length=30, verbose_name=("Name"))
    def __unicode__(self):
        return u'%(name)s' % {"name": self.name}


class Nationality(models.Model):
    """ Info of nationality """
    name = models.CharField(max_length=30, verbose_name=("Name"))
    def __unicode__(self):
        return u'%(name)s' % {"name": self.name}


class Transportation(models.Model):
    """ Info of transportation """
    name = models.CharField(max_length=30, verbose_name=("Name"))
    def __unicode__(self):
        return u'%(name)s' % {"name": self.name}


class Pamper(models.Model):
    """ Camper registered
    """
    title = models.CharField(max_length=2, verbose_name=("Title"))
    first_name = models.CharField(max_length=30, verbose_name=("Prénom"))
    last_name = models.CharField(max_length=30, verbose_name=("Nom"))
    language = models.CharField(max_length=30, verbose_name=("Language"))
    nationality = models.ForeignKey(Nationality, related_name='nationality',\
                                     verbose_name=("Nationalite"))
    city = models.CharField(max_length=30, verbose_name=("Ville"))
    email = models.EmailField(blank=True, verbose_name=("Email"))
    club_name = models.CharField(max_length=50, verbose_name=("Nom du club"))
    zone = models.IntegerField(verbose_name=("Zone"))
    district = models.CharField(max_length=5, verbose_name=("District"))
    country = models.ForeignKey(Country, related_name='country',\
                                     verbose_name=("Pays"))
    date_to_arrive = models.DateField(verbose_name=("Date d'arrivee"),\
                             default=datetime.datetime.today)
    departure_date = models.DateField(verbose_name=("Date de depart"),\
                             default=datetime.datetime.today)
    transportation = models.ForeignKey(Transportation, related_name='transportation',\
                                     verbose_name=("Moyen de transport"))
    def __unicode__(self):
        return u'%(first_name)s %(last_name)s ' % {"first_name": self.first_name,
                                                   "last_name": self.last_name}

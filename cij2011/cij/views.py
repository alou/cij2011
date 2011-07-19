#!/usr/bin/env python
# -*- coding= UTF-8 -*-

from django.core.context_processors import csrf
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import (render_to_response,
                              HttpResponseRedirect, redirect)
from django.core.urlresolvers import reverse
from cij.models import *
from cij.form import PamperForm

def home(request):
    """
    """
    pamper_count = Pamper.objects.all().count()

    return render_to_response('home.html', {'pamper_count': pamper_count})


def registered(request):
    """
    """
    c = {}
    c.update(csrf(request))
    form = PamperForm()
    c.update({'form':form})

    if request.method == 'POST':
        form = PamperForm(request.POST)
        try:

            if 'language' in request.POST and 'title' in request.POST and form.is_valid() :
                print "alou"
                form.save()
                pamper = Pamper.objects.order_by('-id')[0]
                return HttpResponseRedirect(reverse('confirmation', args=[pamper.id]))

            elif 'title' in request.POST and not 'language' in request.POST:
                c.update({'title': request.POST['title']})
            elif 'language' in request.POST and not 'title' in request.POST:
                c.update({'language': request.POST['language']})
            else:
                c.update({'language': request.POST['language'], 'title': request.POST['title']})
            c.update({'form': form})
        except MultiValueDictKeyError:
            c.update({'form': form})
    return render_to_response('registered.html', c)

def confirmation(request, *args, **kwargs):
    """
    """
    num = kwargs["num"] or 1
    c = {}
    pamper = Pamper.objects.filter(id=num)[0]
    print pamper.id
    pamper.url = reverse('correction', args=[pamper.id])
    c.update(csrf(request))
    c.update({'pamper': pamper})
    return render_to_response('confirmation.html', c)

def correction(request, *args, **kwargs):
    """
    """
    num = kwargs["num"] or 1
    c = {}

    form = PamperForm()
    pamper = Pamper.objects.filter(id=num)[0]
    dict = {'title': pamper.title, 'first_name': pamper.first_name, 'last_name': pamper.last_name,
            'language': pamper.language,'nationality': pamper.nationality,'city': pamper.city,
            'email': pamper.email, 'club_name': pamper.club_name, 'zone': pamper.zone,
            'district': pamper.district, 'country': pamper.country, 'date_to_arrive': pamper.date_to_arrive,
            'departure_date': pamper.departure_date, 'transportation': pamper.transportation}
    pamper.title
    form = PamperForm(dict)
    c.update(csrf(request))
    c.update({'form':form, 'language': pamper.language, 'title': pamper.title})
    if request.method == 'POST':
        form = PamperForm(request.POST)
        try:
            if request.POST['date_to_arrive'] :
                day, month ,year = request.POST['date_to_arrive'].split('/')
                if len(day)== 4:
                    anew_format = day + '-' + month + '-' + year
                else:
                    anew_format = year + '-' + month + '-' + day

            if request.POST['departure_date'] :
                day, month ,year = request.POST['departure_date'].split('/')
                if len(day)== 4:
                    dnew_format = day + '-' + month + '-' + year
                else:
                    dnew_format = year + '-' + month + '-' + day

            if 'language' in request.POST and 'title' in request.POST and form.is_valid() :
                pamper.title = request.POST['title']
                pamper.first_name = request.POST['first_name']
                pamper.last_name = request.POST['last_name']
                pamper.language = request.POST['language']
                pamper.nationality = request.POST['nationality']
                pamper.city = request.POST['city']
                pamper.email = request.POST['email']
                pamper.club_name = request.POST['club_name']
                pamper.zone = request.POST['zone']
                pamper.district = request.POST['district']
                pamper.country = request.POST['country']
                pamper.date_to_arrive = anew_format
                pamper.departure_date = dnew_format
                pamper.transportation = form.cleaned_data['transportation']
                pamper.save()
                return HttpResponseRedirect(reverse('confirmation', args=[pamper.id]))

            elif 'title' in request.POST and not 'language' in request.POST:
                c.update({'title': request.POST['title']})
            elif 'language' in request.POST and not 'title' in request.POST:
                c.update({'language': request.POST['language']})
            else:
                c.update({'language': request.POST['language'], 'title': request.POST['title']})
            c.update({'form': form})
        except MultiValueDictKeyError:
            c.update({'form': form})
    return render_to_response('correction.html', c)

def club(request):
    """
    """
    clubs = Club.objects.all()
    c = {}
    c.update(csrf(request))
    c.update({'clubs': clubs})

    return render_to_response('club.html', c)

def contact(request):
    """
    """
    c = {}
    c.update(csrf(request))
    return render_to_response('contact.html', c)

#!/usr/bin/env python
# -*- coding= UTF-8 -*-

from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import (render_to_response,
                              HttpResponseRedirect, redirect)
from django.contrib.auth import (authenticate, login as django_login,
                                 logout as django_logout)
from django.contrib.auth.decorators import login_required

from cij.models import Pamper, Club
from cij.form import PamperForm, LoginForm
from lib.export_xls import liste_des_leo

from datetime import datetime

def home(request):
    """ Page d'accueil """

    pamper_count = Pamper.objects.all().count()
    pamper = ''
    if 'rece' in request.session:
        pamper = request.session.pop('rece')
        print pamper

    return render_to_response('home.html', {'pamper_count': pamper_count, 'pamper': pamper})


def registered(request):
    """ Page d'enregistremet des campers """

    c = {}
    c.update(csrf(request))
    form = PamperForm()
    c.update({'form': form})

    if request.method == 'POST':
        form = PamperForm(request.POST)
        try:

            if 'language' in request.POST and 'title' \
                in request.POST and form.is_valid():
                form.save()
                pamper = Pamper.objects.order_by('-id')[0]
                pamper.receipt = str(pamper.id) + pamper.last_name[0:2] + \
                           pamper.first_name[0:2] + str(pamper.date_to_arrive)
                pamper.save()
                return HttpResponseRedirect(reverse('confirmation',
                                            args=[pamper.id]))
            elif 'title' in request.POST and not 'language' in request.POST:
                c.update({'title': request.POST['title']})
            elif 'language' in request.POST and not 'title' in request.POST:
                c.update({'language': request.POST['language']})
            else:
                c.update({'language': request.POST['language'],
                          'title': request.POST['title']})
            c.update({'form': form})
        except MultiValueDictKeyError:
            c.update({'form': form})

    return render_to_response('registered.html', c)


def confirmation(request, *args, **kwargs):
    """ Page de confirmation """

    num = kwargs["num"] or 1
    c = {}
    pamper = Pamper.objects.filter(id=num)[0]
    pamper.correction = reverse('correction', args=[pamper.id])
    c.update(csrf(request))
    request.session['rece'] = pamper
    c.update({'pamper': pamper})
    return render_to_response('confirmation.html', c)


def correction(request, *args, **kwargs):
    """ Page de correction des informations """
    num = kwargs["num"] or 1
    c = {}

    form = PamperForm()
    pamper = Pamper.objects.filter(id=num)[0]
    dict = {'title': pamper.title, 'first_name': pamper.first_name,
            'last_name': pamper.last_name, 'language': pamper.language,
            'nationality': pamper.nationality, 'city': pamper.city,
            'email': pamper.email, 'club_name': pamper.club_name,
            'zone': pamper.zone, 'district': pamper.district,
            'country': pamper.country, 'date_to_arrive': pamper.date_to_arrive,
            'departure_date': pamper.departure_date,
            'transportation': pamper.transportation}

    form = PamperForm(dict)
    c.update(csrf(request))
    c.update({'form': form, 'language': pamper.language,
              'title': pamper.title})
    if request.method == 'POST':
        form = PamperForm(request.POST)
        try:
            if request.POST['date_to_arrive']:
                day, month, year = request.POST['date_to_arrive'].split('/')
                if len(day) == 4:
                    anew_format = day + '-' + month + '-' + year
                else:
                    anew_format = year + '-' + month + '-' + day

            if request.POST['departure_date']:
                day, month, year = request.POST['departure_date'].split('/')
                if len(day) == 4:
                    dnew_format = day + '-' + month + '-' + year
                else:
                    dnew_format = year + '-' + month + '-' + day

            if 'language' in request.POST and 'title' \
                in request.POST and form.is_valid():
                pamper.title = request.POST['title']
                pamper.first_name = request.POST['first_name']
                pamper.last_name = request.POST['last_name']
                pamper.language = request.POST['language']
                pamper.nationality = form.cleaned_data['nationality']
                pamper.city = request.POST['city']
                pamper.email = request.POST['email']
                pamper.club_name = request.POST['club_name']
                pamper.zone = request.POST['zone']
                pamper.district = request.POST['district']
                pamper.country = form.cleaned_data['country']
                pamper.date_to_arrive = anew_format
                pamper.departure_date = dnew_format
                pamper.transportation = form.cleaned_data['transportation']
                pamper.save()
                return HttpResponseRedirect(reverse('confirmation',
                                                    args=[pamper.id]))
            elif 'title' in request.POST and not 'language' in request.POST:
                c.update({'title': request.POST['title']})
            elif 'language' in request.POST and not 'title' in request.POST:
                c.update({'language': request.POST['language']})
            else:
                c.update({'language': request.POST['language'],
                          'title': request.POST['title']})
            c.update({'form': form})
        except MultiValueDictKeyError:
            c.update({'form': form})

    return render_to_response('correction.html', c)


def club(request):
    """ Liste des clubs du Mali """

    c = {}
    clubs = Club.objects.all()

    c.update(csrf(request))
    c.update({'clubs': clubs})

    return render_to_response('club.html', c)


def login(request):
    """ page de connection """

    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('pampers'))
    else:
        c = {}
        c.update(csrf(request))
        state = "Se connecter"

        form = LoginForm()
        c.update({'form': form, 'state': state})

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return HttpResponseRedirect(reverse('pampers'))
                else:
                    state = "Your Account is not active,\
                                        please contact the site admin."
            else:
                state = u"Votre nom d'utilisateur et / ou \
                                    votre mot de passe est incorrect. \
                                    Veuillez réessayer."
            c.update({'form': form, 'state': state})
    return render_to_response('login.html', c)


def logout(request):
    """ logout est la views qui permet de se deconnecter """

    django_logout(request)
    return redirect("login")


@login_required
def pampers(request, *args, **kwargs):
    """ Page de la liste des campers """

    user = request.user
    num = kwargs["num"] or 1
    pampers = Pamper.objects.all().order_by('-id', '-last_name', '-first_name')

    for pamper in pampers:
        pamper.url_display = reverse('display',
                                         args=[pamper.id])

    paginator = Paginator(pampers, 20)

    page = paginator.page(int(num))
    # si le numero de la page est 2
    page.is_before_first = (page.number == 2)
    # si le numero de la page est egale au numero de l'avant
    # derniere page
    page.is_before_last = (page.number == paginator.num_pages - 1)
    # on constitue l'url de la page suivante
    page.url_next = reverse('pampers', args=[int(num) + 1])
    # on constitue l'url de la page precedente
    page.url_previous = reverse('pampers', args=[int(num) - 1])
    # on constitue l'url de la 1ere page
    page.url_first = reverse('pampers')
    # on constitue l'url de la derniere page
    page.url_last = reverse('pampers',
                            args=[paginator.num_pages])
    c = {'paginator': paginator,
         'user': user,
         'page': page}

    c.update(csrf(request))

    return render_to_response('pampers.html', c)


def contact(request):
    """ Page de contact """

    c = {}
    c.update(csrf(request))
    return render_to_response('contact.html', c)


def display(request, *args, **kwargs):
    """ Page d'affichage des informations sur le camper """

    num = kwargs["id"]
    pamper = Pamper.objects.get(id=num)
    c = {'pamper': pamper}
    c.update(csrf(request))
    c.update({'pamper': pamper})

    return render_to_response('display.html', c)

def ressources(request):
    """ page contenant les docs a telecharger"""
    c = {}
    return render_to_response('ressources.html', c)

@login_required
def export_excel(request):
    from django.http import HttpResponse
    pampers = Pamper.objects.all().order_by('-id', '-last_name', '-first_name')
    file_name = 'listes-des-leos-du-%(date)s a bko.xls' \
                                        % {'date': datetime.now()}
    file_content = liste_des_leo(pampers).getvalue()

    response = HttpResponse(file_content, \
                            content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="%s"' % file_name
    response['Content-Length'] = len(file_content)
    return response

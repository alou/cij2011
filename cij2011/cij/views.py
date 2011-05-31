#!/usr/bin/env python
# -*- coding= UTF-8 -*-

from django.core.context_processors import csrf
from django.shortcuts import (render_to_response,
                              HttpResponseRedirect, redirect)
from django.core.urlresolvers import reverse
from cij.models import *      
from cij.form import PamperForm
                       
def home(request):
    """ 
    """
    pamper_count = Pamper.objects.all().count()
    
    return render_to_response('home.html', {'pamper_count':pamper_count})
    
    
def registered(request):
    """ 
    """
    c = {}
    c.update(csrf(request))
    form = PamperForm()
    c.update({'form':form})
    if request.method == 'POST':
        form = PamperForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
        c.update({'form': form})
    return render_to_response('registered.html', c)
    
    

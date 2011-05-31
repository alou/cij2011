#!/usr/bin/env python
# -*- coding= UTF-8 -*-

from models import *
from django import forms


class PamperForm(forms.ModelForm):

    class Meta:
        model = Pamper
    def __init__(self,  *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        
    def save(self, *args, **kwargs):

        return forms.ModelForm.save(self, *args, **kwargs)

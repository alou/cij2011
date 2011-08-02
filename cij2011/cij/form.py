#!/usr/bin/env python
# -*- coding= UTF-8 -*-

from models import *
from django import forms


class PamperForm(forms.ModelForm):

    class Meta:
        model = Pamper
        exclude = ['title', 'language']
    def __init__(self,  *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.title = self.data['title']
        self.instance.language = self.data['language']
        return forms.ModelForm.save(self, *args, **kwargs)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Username")
    password = forms.CharField(max_length=100, label="Password",\
                               widget=forms.PasswordInput)

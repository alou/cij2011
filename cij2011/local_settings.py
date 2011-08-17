#!/usr/bin/env python
# encoding=utf-8

import os
abs_path = os.path.abspath(__file__)
ROOT_DIR = os.path.dirname(abs_path)

DATABASES = {'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'data_cij.sqlite'}}


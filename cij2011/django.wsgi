#!/usr/bin/env python
# encoding=utf-8
# maintainer: alou

import sys
import site
import os

vepath = '/home/alou/src/envs/cij/lib/python2.7/site-packages'

prev_sys_path = list(sys.path)

# add the site-packages of our virtualenv as a site dir
site.addsitedir(vepath)

sys.path.append('/home/alou/src/cij2011')

# reorder sys.path so new directories from the addsitedir show up first
new_sys_path = [p for p in sys.path if p not in prev_sys_path]
for item in new_sys_path:
    sys.path.remove(item)
sys.path[:0] = new_sys_path

# import from down here to pull in possible virtualenv django install
from django.core.handlers.wsgi import WSGIHandler
os.environ['DJANGO_SETTINGS_MODULE'] = 'cij2011.settings'
application = WSGIHandler()

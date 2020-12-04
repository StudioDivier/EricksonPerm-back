# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1165721/data/www/ericksonperm.ru/EricksonPerm_back')
sys.path.insert(1, '/var/www/u1165721/data/djangoenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'EricksonPerm_back.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
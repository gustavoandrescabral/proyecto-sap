import os
import sys
sys.path = ['/home/gustavo/git/proyecto-sap/sap'] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'sap.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

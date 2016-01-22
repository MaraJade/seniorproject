import sys, os

# The path needs to contain the installed directory (i.e. the directory with
#  this file in it), the parent of the installed directory, wherever your
#  Django install is, plus the system path
# This line is just an example
sys.path = [ '/var/python_apps/', '/var/python_apps/nearby_people/', '/var/python_apps/django-1.0', '/var/python/lib/python2.4' ] + sys.path

# Tell the Django WSGI handler which settings file to bootstap from
os.environ["DJANGO_SETTINGS_MODULE"] = "nearby_people.settings"

# Off we go!
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

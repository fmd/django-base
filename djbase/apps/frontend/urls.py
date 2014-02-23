# Django imports
from django.conf.urls import patterns, include, url

# Local imports
from views import *

urlpatterns = patterns('frontend',
    url(r'^$', home, name='home'),
)
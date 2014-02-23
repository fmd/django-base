from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    
    # Frontend
    url(r'^$', include('djbase.apps.frontend.urls')),

    # Admin 
    url(r'^admin/', include(admin.site.urls)),
)

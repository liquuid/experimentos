from django.conf.urls.defaults import *
from library.views import *
from django.conf import settings
import os

#BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^$', index ),
    (r'^get_track/$',get_tracks),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  os.path.join(settings.SITE_ROOT, 'media/') }),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import patterns, include, url
from ezalor import const
from ezalor.views import identity
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^%s/$' % const.MATCH_PK, identity)
)

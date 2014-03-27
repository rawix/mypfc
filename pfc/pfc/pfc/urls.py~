from django.conf.urls import patterns, include, url
# Enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    # Loading url
    url(r'^loadUniversity/$', 'pfc.views.loadUniversity', name='loadUniversity'),

    # Main url
    url(r'^tuerasmus/$', 'pfc.views.index', name='index'),
    url(r'^contact/$', 'pfc.views.contact', name='contact'),
    url(r'^howto/$', 'pfc.views.howto', name='howto'),

    # User auth urls
    url(r'^accounts/logout/$', 'pfc.views.logout', name='logout'),
    url(r'^accounts/profile/$', 'pfc.views.auth_view', name='auth_view'),
    url(r'^accounts/register/$', 'pfc.views.register', name='register'),
    url(r'^accounts/loggedin/$', 'pfc.views.loggedin', name='loggedin'),
    url(r'^accounts/invalid/$', 'pfc.views.invalid_login', name='invalid_login'),

    # Tuerasmus urls
    url(r'^tuerasmus/', include('tuerasmus.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

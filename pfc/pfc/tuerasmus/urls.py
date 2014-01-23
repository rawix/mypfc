#encoding:utf-8
##########################################################################
# @Author : Rawan Nazmi-Issa Khozouz                                     #
# @Date : 18/09/13.                                                      #
# @Description : Urls to select.                                         #
##########################################################################

# Import objects
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings

from tuerasmus import views

urlpatterns = patterns('',

    # App urls
    url(r'^home/(?P<user>[\S]+)/$', 'tuerasmus.views.home', name='home'),
    url(r'^(?P<user>[\S]+)/myprofile/$', 'tuerasmus.views.myprofile', name='myprofile'), 
    url(r'^(?P<user>[\S]+)/edit_profile/$', 'tuerasmus.views.edit_profile', name='edit_profile'), 
    url(r'^works/$', 'tuerasmus.views.works', name='works'),

    # University urls
    url(r'^uniregister/$', 'tuerasmus.views.uniregister', name='uniregister'),
    url(r'^university/(?P<uni_name>[\S]+)/$', 'tuerasmus.views.university', name='university'),
    url(r'^(?P<user>[\S]+)/myuniversity/(?P<uni_name>[\S]+)/$', 'tuerasmus.views.myuniversity', name='myuniversity'),
    url(r'^universities/$', 'tuerasmus.views.universities', name='universities'),

    # Comments urls
    url(r'^comments/$', 'tuerasmus.views.comments', name='comments'),

    # URLs enabled to view images
    url(r'^media/(?P<path>.*)/$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),

)

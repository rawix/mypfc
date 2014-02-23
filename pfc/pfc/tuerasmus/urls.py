#encoding:utf-8
##########################################################################
# @Author : Rawan Nazmi-Issa Khozouz                                     #
# @Date : 18/09/13.                                                      #
# @Description : Urls to select.                                         #
##########################################################################

# Import objects
from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static

from tuerasmus import views

urlpatterns = patterns('',

    # Universities urls
    url(r'^uniregister/$', 'tuerasmus.views.uniregister', name='uniregister'),
    url(r'^uniedit/(?P<uni_name>[\S]+)/(?P<type_form>[\S]+)/$', 'tuerasmus.views.unieditform', name='unieditform'),
    url(r'^university/(?P<uni_name>[\S]+)/(?P<type_info>[\S]+)/$', 'tuerasmus.views.uninfo', name='uninfo'),
    url(r'^universities/$', 'tuerasmus.views.universities', name='universities'),
    url(r'^uniedit/(?P<uni_name>[\S]+)/$', 'tuerasmus.views.uniedit', name='uniedit'),
    url(r'^university/(?P<uni_name>[\S]+)/$', 'tuerasmus.views.university', name='university'),

    # All users
    url(r'^urerasmus/$', 'tuerasmus.views.urerasmus', name='urerasmus'),

    # Comments urls
    url(r'^comments/$', 'tuerasmus.views.comments', name='comments'),

    # Users urls
    url(r'^(?P<user>[\S]+)/myprofile/$', 'tuerasmus.views.myprofile', name='myprofile'), 
    url(r'^(?P<user>[\S]+)/edit_profile/$', 'tuerasmus.views.edit_profile', name='edit_profile'), 
    url(r'^(?P<user>[\S]+)/myuniversity/$', 'tuerasmus.views.myuniversity', name='myuniversity'),
    url(r'^(?P<user>[\S]+)/myerasmus/$', 'tuerasmus.views.myerasmus', name='myerasmus'),
    url(r'^(?P<user>[\S]+)/$', 'tuerasmus.views.home', name='home'),
    
    # URLs enabled to view images
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),

)

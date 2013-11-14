from django.conf.urls import patterns, include, url

from . import views 


urlpatterns = patterns('',
    url(r'^(?P<exp_slug>[-\w]+)/$', views.view_expertcategory, name='index'),
    url(r'^(?P<exp_slug>[-\w]+)/(?P<matchup_slug>[-\w]+)/$', 
    	views.view_expertpicks, name='detail'),

)

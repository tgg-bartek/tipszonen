from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

from . import views 

admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^admin/', include(admin.site.urls)),
    # always keep in first in relation to /accounts/ url pattern
    # othweside it won't overwrite it
    url(r'^accounts/login/$', views.login, name="auth_login"), 
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'', include('blog.urls', namespace='blog')),
    url(r'experts/', include('picks.urls', namespace='picks')),
    
)

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import admin

from . import views 

admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    # dunno why but keep this link on top of accounts/, it breaks otherwise
     
    # always keep in first in relation to /accounts/ url pattern
    # otherwise it won't overwrite it
    url(r'^accounts/login/$', views.login, name="auth_login"),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'edit_details/$', login_required(views.UserProfileEditView.as_view()),
        name='edit_details'),
    url(r'', include('blog.urls', namespace='blog')),
    url(r'experts/', include('picks.urls', namespace='picks')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^users/(?P<slug>\w+)/$', views.UserProfileDetailView.as_view(),
    	name='profile'),
    
)

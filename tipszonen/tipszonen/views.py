from django.contrib.auth import views as auth_views


# Adds ``Remember Me`` functionality. By detaul Django session
# expires after 2 weeks, or you can define SESSION_COOKIE_AGE in settings.py
# If a user checkboxs, it will be so. Otherwise set_expiry(0) makes it 
# a one-off login.
def login(request, *args, **kwargs):
	if request.method == 'POST':
		if not request.POST.get('remember_me', None):
			request.session.set_expiry(0)
	return auth_views.login(request, *args, **kwargs)



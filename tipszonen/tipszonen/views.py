from django.contrib.auth import views as auth_views
from django.contrib.auth import get_user_model
from django.views.generic import DetailView 
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse

from .models import UserProfile
from .forms import UserProfileForm

def login(request, *args, **kwargs):
	"""``Remember Me`` functionality. By detaul Django session lasts 2 weeks, 
	or you can define SESSION_COOKIE_AGE in settings.py. If a user checkboxs, 
	it will be so. Otherwise set_expiry(0) makes it a one-off login.
	"""
	if request.method == 'POST':
		if not request.POST.get('remember_me', None):
			request.session.set_expiry(0)
	return auth_views.login(request, *args, **kwargs)


class UserProfileDetailView(DetailView):
	model = get_user_model()
	slug_field = 'username'
	template_name = 'tipszonen/user_detail.html'

	# Make sure it always creates the User profile before retreiving
	def get_object(self, queryset=None):
		user = super(UserProfileDetailView, self).get_object(queryset)
		UserProfile.objects.get_or_create(user=user)
		return user 

class UserProfileEditView(UpdateView):
	model = UserProfile
	form_class = UserProfileForm
	template_name = 'tipszonen/edit_profile.html'

	# override get_object to make sure a user can't change
	# somebody else's profile but his own
	def get_object(self, queryset=None):
		return UserProfile.objects.get_or_create(user=self.request.user)[0]

	def get_success_url(self):
		return reverse('profile', kwargs={'slug': self.request.user})





from django.db import models 
from django.contrib.auth.models import User 


class UserProfile(models.Model):
	user = models.OneToOneField(User, unique=True)
	# Extra attributes
	bio = models.TextField(null=True)

	def __unicode__(self):
		return self.user 

def create_profile(sender, instance, created, **kwargs):
	if created:
		profile, created = UserProfile.objects.get_or_create(user=instance)

from django.db.models.signals import post_save
post_save.connect(create_profile, sender=User)


from django.contrib.auth.models import User 
from django.template.defaultfilters import slugify
from django.db import models


class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, blank=True, default='', help_text='''
			Populates automatically. It's advisable you do not change it.''')
	content = models.TextField()
	published = models.BooleanField(default=True) 
	author = models.ForeignKey(User)

	class Meta:
		ordering = ['-created_at', 'title']

	def __unicode__(self):
		return self.title 

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)


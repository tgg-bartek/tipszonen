from django.views.generic import ListView, DetailView

from .models import Post 


class PublishPostsMixin(object):
	'Return posts ticked as published'
	def get_queryset(self):
		queryset = super(PublishPostsMixin, self).get_queryset()
		return queryset.filter(published=True)


class PostListView(PublishPostsMixin, ListView):
	model = Post 
	template_name = 'blog/index.html'
	context_object_name = 'published_post_list'

class PostDetailView(PublishPostsMixin, DetailView):
	model = Post 
	template_name = 'blog/detail.html'


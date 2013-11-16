from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404 

from .models import Pick, ExpertCategory


def view_expertcategory(request, exp_slug):
	exp_cat = get_object_or_404(ExpertCategory, slug=exp_slug)
	template_name = 'picks/index.html'
	pick_list = Pick.objects.filter(published=True, expert=exp_cat.pk)

	context = {
		'pick_list': pick_list,
	}

	return render(request, template_name, context)


def view_expertpicks(request, exp_slug, matchup_slug):
	template_name = 'picks/detail.html'
	pick = get_object_or_404(Pick, slug=matchup_slug)
	
	context = {
		'pick': pick,
	}

	return render(request, template_name, context)


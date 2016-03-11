from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView

class HomePageView(TemplateView):
    template_name = "home.html"

class FAQView(TemplateView):
    template_name = "faq.html"

class SightingExpertCommentsView(ListView):
    template_name = "sighting_expert_comments.html"

class SightingView(DetailView):
    template_name = "sighting.html"

class SightingsView(ListView):
    template_name = "sightings.html"

class SightQuestionView(DetailView):
    template_name = "sight_question.html"

class LocationsPageView(TemplateView):
    template_name = "locations.html"

class SightingCommentsView(ListView):
	template_name = "sighting_comments.html"
	
class SightExpertCommentView(DetailView):
	template_name = "sight_expert_comment.html"

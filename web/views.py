from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from api.models import SightingFAQ

class HomePageView(TemplateView):
    template_name = "home.html"

class FAQView(ListView):
    template_name = "faq.html"
    model = SightingFAQ

class SightingExpertCommentsView(TemplateView):
    template_name = "sighting_expert_comments.html"

class SightingView(TemplateView):
    template_name = "sighting.html"

class SightingsView(TemplateView):
    template_name = "sightings.html"

class SightQuestionView(TemplateView):
    template_name = "sight_question.html"

class LocationsPageView(TemplateView):
    template_name = "locations.html"

class SightingCommentsView(TemplateView):
	template_name = "sighting_comments.html"

class SightExpertCommentView(TemplateView):
	template_name = "sight_expert_comment.html"

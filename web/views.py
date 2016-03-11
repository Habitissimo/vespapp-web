from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from api.models import Sighting
from api.models import ExpertComment

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

	def get_object(self, queryset=None):
		sighting_id = self.kwargs.get('sighting_id')
		expert_comment_id = self.kwargs.get('expert_comment_id')
		
		sighting = Sighting.objects.get(pk=sighting_id)
		expert_comment = ExpertComment.objects.get(pk=expert_comment_id)

		if str(expert_comment.sighting.id) != str(sighting_id):
			return None

		return expert_comment
        

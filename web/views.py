from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from api.models import SightingFAQ
from api.models import Sighting
from api.models import UserComment


class HomePageView(TemplateView):
    template_name = "home.html"

class FAQView(ListView):
    template_name = "faq.html"
    model = SightingFAQ

class SightingExpertCommentsView(ListView):
    template_name = "sighting_expert_comments.html"

class SightingView(DetailView):
    template_name = "sighting.html"
    pk_url_kwarg= "sighting_id"
    model= Sighting

class SightingsView(ListView):
    template_name = "sightings.html"
    model = Sighting# Defino el modelo que utilizo
    context_object_name = "sightings_list"# Defino la lista donde se cargan los objetos del modelo
    paginate_by = 50  # Control de la paginacion

    def get_queryset(self, **kwargs):
     	return Sighting.objects.all()


class SightQuestionView(DetailView):
    template_name = "sight_question.html"

class LocationsPageView(TemplateView):
    template_name = "locations.html"

class SightingCommentView(DetailView):
    template_name = "sighting_comment.html"
    template_name_field = 'object'
    model = UserComment
      
    def get_object(self, queryset=None):
        sighting_id = self.kwargs.get('sighting_id')
        comment_id = self.kwargs.get('comment_id')

        sighting = Sighting.objects.get(pk=sighting_id)
        comment = UserComment.objects.get(pk=comment_id)

        if str(comment.sighting.id) != str(sighting_id):
            return None

        return comment


class SightingCommentsView(ListView):
	template_name = "sighting_comments.html"
	
class SightExpertCommentView(DetailView):
	template_name = "sight_expert_comment.html"

class SightingExpertCommentsView(ListView):
    template_name = "sighting_expert_comments.html"

class NewSightingView(TemplateView):
	template_name = "new_sighting.html"
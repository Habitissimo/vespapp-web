from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

class FAQView(TemplateView):
    template_name = "faq.html"

#class SightingExpertCommentsView(TemplateView):
#    template_name = "sighting_expert_comments.html"
#    def get_context_data(self, **kwargs):
#        sighting_id = sighting.objects.get(id=kwargs['sighting_id'])
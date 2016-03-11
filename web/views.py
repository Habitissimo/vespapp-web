from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

class SightingView(TemplateView):
    template_name = "sighting.html"
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

class SightingsView(TemplateView):
    template_name = "sightings.html"


class SightQuestionView(TemplateView):
    template_name = "sight_question.html"
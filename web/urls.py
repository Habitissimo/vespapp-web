from django.conf.urls import url
from web import views
from web.views import HomePageView
from web.views import SightingView


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),

    url(r'^sighting/(?P<sighting_id>[0-9]+)/$', SightingView.as_view(), name="sighting_id"),


#    url(r'^sightings/$', views.sightings),
#
#    url(r'^sightings/(?P<sighting_id>[0-9]+)/$',
#        views.sighting),
#    url(r'^sightings/(?P<sighting_id>[0-9]+)/photos/$',
#        views.sighting_photos),
#
#    url(r'^sightings/(?P<sighting_id>[0-9]+)/expert_comments/$',
#        views.sighting_expert_comments),
#    url(r'^sightings/(?P<sighting_id>[0-9]+)/expert_comments/(?P<expert_comment_id>[0-9]+)$',
#        views.sighting_expert_comment),
#
#    url(r'^sightings/(?P<sighting_id>[0-9]+)/questions/$',
#        views.sighting_questions),
#    url(r'^sightings/(?P<sighting_id>[0-9]+)/questions/(?P<question_id>[0-9]+)$',
#        views.sighting_question),
#
#    url(r'^locations/$',
#        views.locations),
]

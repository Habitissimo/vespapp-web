from django.conf.urls import url
from web import views
from web.views import HomePageView
from web.views import FAQView
from web.views import SightingExpertCommentsView
from web.views import SightingView
from web.views import SightingsView
from web.views import SightQuestionView
from web.views import LocationsPageView
from web.views import SightingCommentView
from web.views import SightingCommentsView
from web.views import SightExpertCommentView
from web.views import NewSightingView


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^faq/$', FAQView.as_view(), name='faq'),
    url(r'^locations/$', LocationsPageView.as_view(), name='locations'),
    url(r'^new_sighting/$', NewSightingView.as_view(), name='new_sighting'),   
    url(r'^sighting/(?P<sighting_id>[0-9]+)/expert_comments/$',
    	SightingExpertCommentsView.as_view(), name='sighting_expert_comments'),
    url(r'^sighting/(?P<sighting_id>[0-9]+)/$', SightingView.as_view(), name="sighting_id"),
    url(r'^sightings/$', SightingsView.as_view(), name='sightings'),
    url(r'^sight_question/(?P<sighting_id>[0-9]+)/$', SightQuestionView.as_view(), name='sight_question'),

    url(r'^locations/$', LocationsPageView.as_view(), name='locations'),

    url(r'^sighting/(?P<sighting_id>[0-9]+)/user_comments/$', SightingCommentsView.as_view(), name='sighting_comments'),
    url(r'^sighting/(?P<sighting_id>[0-9]+)/user_comment/(?P<comment_id>[0-9]+)/$', SightingCommentView.as_view(), name='sighting_comment'),

    url(r'^sighting/(?P<sighting_id>[0-9]+)/expert_comments/$', SightingExpertCommentsView.as_view(), name='sighting_expert_comments'),
    url(r'^sighting/(?P<sighting_id>[0-9]+)/expert_comments/(?P<expert_comment_id>[0-9]+)$', SightExpertCommentView.as_view(), name='sight_expert_comment'),
]

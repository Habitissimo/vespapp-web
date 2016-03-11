from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from api.models import Sighting, Picture
from api.serializers import SightingSerializer, PictureSerializer
from api.models import Sighting, UserComment, ExpertComment
from api.serializers import SightingSerializer, UserCommentSerializer, ExpertCommentSerializer

#Sightings
class SightingListCreateView(ListCreateAPIView):
    serializer_class = SightingSerializer

    def get_queryset(self):
        return Sighting.objects.order_by('-created_at')


class SightingRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = SightingSerializer
    queryset = Sighting.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'sighting_id'

#Picture
class SightingPictureCreateView(ListCreateAPIView):
    serializer_class = PictureSerializer

    def get_queryset(self):
        sighting_id = self.kwargs.get('sighting_id')
        return Picture.objects.filter(sighting__pk=sighting_id)

    def create(self, request, *args, **kwargs):
        request.data['sighting'] = kwargs.get('sighting_id')
        return super().create(request, *args, **kwargs)

#Comments
class SightingUserCommentCreateView(ListCreateAPIView):
    serializer_class = UserCommentSerializer

    def get_queryset(self):
        sighting_id = self.kwargs.get('sighting_id')
        return UserComment.objects.filter(sighting__pk=sighting_id)

    def create(self, request, *args, **kwargs):
        request.data['sighting'] = kwargs.get('sighting_id')
        return super().create(request, *args, **kwargs)


class SightingExpertCommentListCreateView(ListCreateAPIView):
    serializer_class = UserCommentSerializer

    def get_queryset(self):
        sighting_id = self.kwargs.get('sighting_id')
        return ExpertComment.objects.filter(sighting__pk=sighting_id)

    def create(self, request, *args, **kwargs):
        request.data['sighting'] = kwargs.get('sighting_id')
        return super().create(request, *args, **kwargs)

#Locations
class LocationsList(ListAPIView):
    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects;

#Questions&Answers
class SightingQuestionsListView(ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        sighting_id = self.kwargs.get('sighting_id')
        sighting_type = Sighting.objects.filter(id=sighting_id)
        return Question.objects.filter(sighting_type=sighting_type)

class SightingAnswerRetrieveUpdate(RetrieveUpdateAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        sighting_id = self.kwargs.get('sighting_id')
        sighting_type = Sighting.objects.filter(id=sighting_id)
        questions = Question.objects.filter(type=sighting_type)
        answers = Answer.objects.filter(question IN questions)

class SightingQuestionsCreateView(ListCreateAPIView):
    serializer_class = UserCommentSerializer

    def get_queryset(self):
        sighting_id = self.kwargs.get('sighting_id')
        return ExpertComment.objects.filter(sighting__pk=sighting_id)

    def create(self, request, *args, **kwargs):
        request.data['sighting'] = kwargs.get('sighting_id')
        return super().create(request, *args, **kwargs)

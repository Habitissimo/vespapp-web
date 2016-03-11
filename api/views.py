from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from api.models import Sighting, Picture
from api.serializers import SightingSerializer, PictureSerializer
from api.models import Sighting, UserComment, ExpertComment
from api.serializers import SightingSerializer, UserCommentSerializer, ExpertCommentSerializer


class SightingListCreateView(ListCreateAPIView):
    serializer_class = SightingSerializer

    def get_queryset(self):
        return Sighting.objects.order_by('-created_at')


class SightingRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = SightingSerializer
    queryset = Sighting.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'sighting_id'


class SightingPictureCreateView(ListCreateAPIView):
    serializer_class = PictureSerializer

    def get_queryset(self):
        sighting_id = self.kwargs.get('sighting_id')
        return Picture.objects.filter(sighting__pk=sighting_id)

    def create(self, request, *args, **kwargs):
        request.data['sighting'] = kwargs.get('sighting_id')
        return super().create(request, *args, **kwargs)


class SightingUserCommentsView(ListCreateAPIView):
    serializer_class = UserCommentSerializer

    def get_queryset(self):
        sighting_id = self.kwargs['sighting_id']
        comments = UserComment.objects.filter(sighting=sighting_id)
        return comments

    def post(self, sighting_id):
        #sighting_id = self.kwargs['sighting_id']

        if not Sighting.objects.exists(id=sighting_id):
            return None

        sighting = Sighting.objects.get(id=sighting_id)

        new_comment = UserComment(
                body='pruebahehehe',
                sighting=sighting,
        )

        new_comment.save()

        return new_comment


class SightingUserCommentView(ListCreateAPIView):
    serializer_class = UserCommentSerializer

    def get_queryset(self):
        sighting_id = self.kwargs['sighting_id']
        comments = UserComment.objects.filter(sighting=sighting_id)
        return comments

    def post(self, sighting_id):
        #sighting_id = self.kwargs['sighting_id']

        if not Sighting.objects.exists(id=sighting_id):
            return None

        sighting = Sighting.objects.get(id=sighting_id)

        new_comment = UserComment(
                body='pruebahehehe',
                sighting=sighting,
        )

        new_comment.save()

        return new_comment

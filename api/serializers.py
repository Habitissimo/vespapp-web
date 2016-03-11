from rest_framework import serializers
from api.models import Sighting, Picture, UserComment, ExpertComment, Question, Answer

class SightingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sighting


class UserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserComment


class ExpertCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpertComment


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer

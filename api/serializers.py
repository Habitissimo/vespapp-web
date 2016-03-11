from rest_framework import serializers


class Sighting:
    pass


class SightingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sighting

from rest_framework import serializers
from .models import Marker, UserMarker


class MarkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marker
        fields = '__all__'


class UserMarkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMarker
        fields = '__all__'

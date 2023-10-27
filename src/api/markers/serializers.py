from rest_framework import serializers

from api.users.models import CustomUser


class MarkerSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(),required=False)
    name = serializers.CharField()
    brand = serializers.CharField()
    model = serializers.CharField()
    serial_number = serializers.CharField()
    details = serializers.CharField()

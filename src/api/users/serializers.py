from rest_framework import serializers
from api.users.models import CustomUser, Session


class UserCreateSerializer(serializers.ModelSerializer):
    session = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('id',
                  'email',
                  'first_name',
                  'last_name',
                  'username',
                  'google_id',
                  'session'
                  )

    def get_session(self, user):
        session = Session.objects.get(user=user)
        return {
            "id": session.id,
            "access_token": session.access_token,
            "refresh_token": session.refresh_token,
            "active": session.active,
            "generation_date": session.generation_date,
            "expiration_date": session.expiration_date,
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation

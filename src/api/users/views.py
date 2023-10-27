from django.db import transaction

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from google.oauth2 import id_token
from google.auth.transport import requests

from api.users.models import CustomUser
from api.users.serializers import UserCreateSerializer
from api.users.functions import generate_session


class UserAuthGoogleAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        credential = request.data.get('credential')

        try:
            id_info = id_token.verify_oauth2_token(credential, requests.Request())

            user_data = {
                'email': id_info.get('email'),
                'first_name': id_info.get('given_name'),
                'last_name': id_info.get('family_name'),
                'username': id_info.get('name'),
                'google_id': id_info.get('sub')
            }

            with transaction.atomic():
                user, created = CustomUser.objects.get_or_create(email=user_data['email'], defaults=user_data)

                if not created:
                    user.first_name = user_data['first_name']
                    user.last_name = user_data['last_name']
                    user.username = user_data['username']
                    user.google_id = user_data['google_id']
                    user.save()

                    serializer = self.serializer_class(user)
                    return Response({"user": serializer.data})

                generate_session(user)
                serializer = self.serializer_class(user)
                return Response({"user": serializer.data},
                                status.HTTP_200_OK)

        except ValueError:
            return Response({"message": "Invalid credential"},
                            status.HTTP_403_FORBIDDEN)

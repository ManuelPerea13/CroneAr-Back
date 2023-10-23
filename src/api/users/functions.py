from django.utils import timezone
from django.conf import settings

from rest_framework_simplejwt.tokens import RefreshToken

from api.users.models import Session


def generate_session(user):
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)
    active = True
    generation_date = timezone.now()
    expiration_date = timezone.now() + settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']
    session = Session.objects.create(
        user=user,
        access_token=access_token,
        refresh_token=refresh_token,
        active=active,
        generation_date=generation_date,
        expiration_date=expiration_date
    )
    return session

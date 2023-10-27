from django.urls import path
from api.users.views import UserAuthGoogleAPIView

urlpatterns = [
    path('auth/', UserAuthGoogleAPIView.as_view()),
]

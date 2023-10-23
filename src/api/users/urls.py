from django.urls import path
from api.users.views import GoogleAuthAPIView

urlpatterns = [
    path('users/google-auth/', GoogleAuthAPIView.as_view()),
]

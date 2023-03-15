from django.urls import path

from api.users.views import hello

urlpatterns = [
    path('users/',  UserCreate.as_view()),
]
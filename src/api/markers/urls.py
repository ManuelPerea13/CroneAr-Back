from django.urls import path
from api.markers.views import MarkerCreate

urlpatterns = [
    path('markers/', MarkerCreate.as_view()),
]

from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

api_patterns = ([
    path('', include('api.users.urls')),
    path('', include('api.markers.urls')),
])

token_pattern = ([
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
])

urlpatterns = [
    path('', include(token_pattern)),
    path('', include(api_patterns)),
    path('admin/', admin.site.urls),
]

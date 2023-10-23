from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import Marker
from .serializers import MarkerSerializer, UserMarkerSerializer
from api.users.models import CustomUser

class MarkerCreate(CreateAPIView):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer

    def create(self, request, *args, **kwargs):
        # print(request.data)
        marker_serializer = self.get_serializer(data=request.data)
        # print(marker_serializer)
        marker_serializer.is_valid(raise_exception=True)
        marker = marker_serializer.save()
        
        user_id = request.data['user']
        user = CustomUser.objects.get(pk=user_id)

        user_marker_data = {
            'user': user.id,
            'marker': marker.id,
        }

        user_marker_serializer = UserMarkerSerializer(data=user_marker_data)
        user_marker_serializer.is_valid(raise_exception=True)
        user_marker_serializer.save()

        return Response({'message': 'Marker and UserMarker created successfully'},
                        status.HTTP_201_CREATED)

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import Marker
from .serializers import MarkerSerializer
from api.users.models import CustomUser


class MarkerCreate(CreateAPIView):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer

    def create(self, request, *args, **kwargs):

        marker_serializer = self.get_serializer(data=request.data)

        if marker_serializer.is_valid(raise_exception=True):
            user = CustomUser.objects.get(pk=request.data['user'])
            name = request.data['name']
            brand = request.data['brand']
            model = request.data['model']
            serial_number = request.data['serial_number']
            details = request.data['details']
            
            marker = Marker.objects.create(
                user=user,
                name=name,
                brand=brand,
                model=model,
                serial_number=serial_number,
                details=details,
                update=
            )

            print(marker)

        return Response({"message": "Marker created successfully"},
                        status.HTTP_201_CREATED)

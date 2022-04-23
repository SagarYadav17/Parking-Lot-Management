# Django & Rest Framework imports
from rest_framework.viewsets import ModelViewSet

# models
from business.models import ParkingLot

# serializers
from business.serializers import ParkingLotSerializer


class ParkingLotViewSet(ModelViewSet):
    serializer_class = ParkingLotSerializer

    def get_queryset(self):
        queryset = ParkingLot.objects.filter(user=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        request.data["user"] = self.request.user.id
        return super().create(request, *args, **kwargs)

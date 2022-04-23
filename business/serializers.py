from rest_framework.serializers import ModelSerializer

from business.models import ParkingLot, ParkingLotPrice


class ParkingLotSerializer(ModelSerializer):
    class Meta:
        model = ParkingLot
        fields = "__all__"


class ParkingLotPriceSerializer(ModelSerializer):
    parking_lot_detail = ParkingLotSerializer(source="parking_lot", read_only=True)

    class Meta:
        model = ParkingLotPrice
        fields = "__all__"

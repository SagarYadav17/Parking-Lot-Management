from django.urls import path, include
from rest_framework.routers import DefaultRouter

from business.views import ParkingLotViewSet

router = DefaultRouter()

router.register("parking-lots", ParkingLotViewSet, basename="business-parking-lot")

urlpatterns = [
    path("", include(router.urls)),
]

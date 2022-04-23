from django.db import models
from django.contrib.auth.models import User

VEHICLE_TYPE_CHOICES = (
    ("Two Wheeler", "Two Wheeler"),
    ("Car/Jeep/Van", "Car/Jeep/Van"),
    ("LCV/Mini-Bus", "LCV/Mini-Bus"),
    ("Bus/Truck", "Bus/Truck"),
    ("Multi-Axle", "Multi-Axle"),
)

DURATION = (
    ("0-6 Hours", "0-6 Hours"),
    ("6-12 Hours", "6-12 Hours"),
    ("Day", "Day"),
    ("Week", "Week"),
    ("Month", "Month"),
    ("Year", "Year"),
)


class ParkingLot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    latitude = models.FloatField(default=None)
    longitude = models.FloatField(default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ParkingLotPrice(models.Model):
    parking_lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    duration = models.CharField(max_length=100, choices=DURATION)
    vehicle_type = models.CharField(max_length=100, choices=VEHICLE_TYPE_CHOICES)

    class Meta:
        unique_together = (("parking_lot", "duration", "vehicle_type"),)

    def __str__(self):
        return self.parking_lot.name

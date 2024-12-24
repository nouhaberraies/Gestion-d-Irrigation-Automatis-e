from rest_framework import serializers
from .models import IrrigationZone

class IrrigationZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = IrrigationZone
        fields = ['id', 'name', 'soil_moisture', 'status']

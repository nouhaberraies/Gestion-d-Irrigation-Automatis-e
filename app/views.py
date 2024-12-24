from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import IrrigationZone
from .serializers import IrrigationZoneSerializer

# Ajouter une zone d'irrigation dans le base pour les tests 
@api_view(['POST'])
def add_zone_irrigation(request):
    serializer = IrrigationZoneSerializer(data=request.data)
    if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# fct qui affiche les listes des zones
@api_view(['GET'])
def liste_zones_irrigation(request):
    zones = IrrigationZone.objects.all()
    serializer = IrrigationZoneSerializer(zones, many=True)
    return Response(serializer.data)


# fct pour la màj des status selon soil
@api_view(['POST'])
def modifier_zone_irrigation(request, zone_id):
    #recuperation de zone par id
    try:
        zone = IrrigationZone.objects.get(id=zone_id) 
    except IrrigationZone.DoesNotExist:
        return Response({"error": "Zone non trouvée"}, status=status.HTTP_404_NOT_FOUND)
    #creation d'un nouvel soil
    nouvel_soil_moisture = request.data.get('soil_moisture')
    if nouvel_soil_moisture is not None:
        zone.soil_moisture = nouvel_soil_moisture  
    zone.save() # appel au fct save qui se trouve dans le models.py

    return Response({"message": "Zone mise à jour avec succès"}, status=status.HTTP_200_OK)

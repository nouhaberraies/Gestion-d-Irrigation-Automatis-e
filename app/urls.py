from django.urls import path
from . import views

urlpatterns = [
    path('api/irrigation/ajouter/', views.add_zone_irrigation, name='add_zone_irrigation'),
    path('api/irrigation/liste/', views.liste_zones_irrigation, name='liste_zones_irrigation'),
    path('api/irrigation/zones/modifier/<int:zone_id>/', views.modifier_zone_irrigation, name='modifier_zone_irrigation'),
]

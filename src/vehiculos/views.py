from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework import status

from .models import Vehiculo, Equipamiento
from .serializers import VehiculoSerializer, EquipamientoSerializer


#----- vistas genericas concretas basadas en clases para equipamiento -----#

class EquipamientoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Equipamiento.objects.all()
    serializer_class = EquipamientoSerializer

class EquipamientoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipamiento.objects.all()
    serializer_class = EquipamientoSerializer

#----- vistas genericas concretas basadas en clases para vehiculo ------#

class VehiculoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class VehiculoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

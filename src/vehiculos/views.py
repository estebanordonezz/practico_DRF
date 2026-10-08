from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Vehiculo, Equipamiento
from .serializers import VehiculoSerializer, EquipamientoSerializer


class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [IsAuthenticated]  # # noqa: RUF012

class EquipamientoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Equipamiento.objects.all()
    serializer_class = EquipamientoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # # noqa: RUF012


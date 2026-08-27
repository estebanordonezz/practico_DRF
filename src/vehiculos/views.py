from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Vehiculo
from .serializers import VehiculoSerializer

@api_view(["GET", "POST"])
def vehiculos(request):
    if request.method == "GET":
        vehiculos = Vehiculo.objects.all()
        serializer = VehiculoSerializer(vehiculos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = VehiculoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"mensaje: Vehiculo Registrado"}, status=status.HTTP_201_CREATED,
            )
        return Response(
            {"mensaje: No se pudo registrar el vehiculo"}, status=status.HTTP_400_BAD_REQUEST,
        )

@api_view(["GET", "PUT", "DELETE"])
def vehiculos_detail(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)

    if request.method == "GET":
        serializer = VehiculoSerializer(vehiculo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        serializer = VehiculoSerializer(vehiculo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"mensaje: Vehiculo Actualizado"}, status=status.HTTP_200_OK,
            )
        return Response(
            {"mensaje: No se pudo actualizar"}, status=status.HTTP_400_BAD_REQUEST,
        )

    if request.method == "DELETE":
        vehiculo.delete()
        return Response(
            {"mensaje: Vehiculo Eliminado"}, status=status.HTTP_200_OK,
        )
    return Response(
            {"mensaje": "No se pudo eliminar"}, status=status.HTTP_400_BAD_REQUEST,
    )


from rest_framework import serializers
from .models import Vehiculo

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = [ # noqa: RUF012
            "id",
            "tipo_vehiculo", 
            "marca",
            "modelo",
            "precio",
            "color" ,
            "version",
            "kilometraje",
            "fecha_carga",
        ]
        read_only_fields = ["id", "fecha_carga"] # noqa: RUF012
        
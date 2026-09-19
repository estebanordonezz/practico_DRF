from rest_framework import serializers
from .models import Vehiculo, Equipamiento

class EquipamientoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipamiento 
        fields = [  # noqa: RUF012
            "id",
            "nombre",
            "descripcion",
        ]
        read_only_fields = ["id"] # noqa: RUF012

class VehiculoSerializer(serializers.ModelSerializer):

    equipamientos = EquipamientoSerializer(many=True, read_only=True)
    equipamientos_ids = serializers.PrimaryKeyRelatedField(
        queryset=Equipamiento.objects.all(),
        source='equipamientos',
        many=True,
        write_only=True,
        required=False
    )
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
            "equipamientos",
            "equipamientos_ids",
        ]
        read_only_fields = ["id", "fecha_carga"] # noqa: RUF012
        
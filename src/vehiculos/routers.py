from rest_framework.routers import DefaultRouter    
from .views import VehiculoViewSet, EquipamientoViewSet

router = DefaultRouter()

router.register(r'vehiculos', VehiculoViewSet, basename='vehiculo')
router.register(r'equipamientos', EquipamientoViewSet, basename='equipamiento')
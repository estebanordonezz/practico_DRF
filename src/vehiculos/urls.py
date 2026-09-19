from django.urls import path 
from .views import (
    VehiculoListCreateAPIView, 
    VehiculoRetrieveUpdateDestroyAPIView, 
    EquipamientoListCreateAPIView, 
    EquipamientoRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('vehiculos/', VehiculoListCreateAPIView.as_view(), name='vehiculos_api'),
    path('vehiculos/<int:pk>/', VehiculoRetrieveUpdateDestroyAPIView.as_view(), name='vehiculos_detail_api'),
    
    path('equipamientos/', EquipamientoListCreateAPIView.as_view(), name='equipamientos_api'),
    path('equipamientos/<int:pk>/', EquipamientoRetrieveUpdateDestroyAPIView.as_view(), name='equipamientos_detail_api')
]

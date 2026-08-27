from django.urls import path 
from .views import vehiculos, vehiculos_detail

urlpatterns = [
    path('', vehiculos, name='vehiculos_api'),
    path('<int:pk>/', vehiculos_detail, name='vehiculos_detail_api')
]
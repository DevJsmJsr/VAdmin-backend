from django.urls import path

from .views import (PersonListAPIView,PropertyCardAPIView, VehicleAPIView,
                    VehicleEngineListCreateView, VehicleEngineRetrieveUpdateDestroyView,
                    VehicleAccessoriesListCreateView, VehicleAccessoriesRetrieveUpdateDestroyView)

urlpatterns = [
    path('persons/', PersonListAPIView.as_view(), name='persons'),
    path('property-cards/', PropertyCardAPIView.as_view(), name='property-cards'),
    path('vehicle/', VehicleAPIView.as_view(), name='vehicle'),
    path('vehicle-engines/', VehicleEngineListCreateView.as_view(), name='vehicle-engine-list-create'),
    path('vehicle-engines/<int:pk>/', VehicleEngineRetrieveUpdateDestroyView.as_view(), name='vehicle-engine-detail'),
    path('vehicle-accessories/', VehicleAccessoriesListCreateView.as_view(), name='vehicle-accessories-list-create'),
    path('vehicle-accessories/<int:pk>/', VehicleAccessoriesRetrieveUpdateDestroyView.as_view(), name='vehicle-accessories-detail'),
]
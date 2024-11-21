from django.urls import path

from .views import (PersonListAPIView,PropertyCardAPIView, VehicleAPIView,
                    VehicleEngineListCreateView, VehicleEngineRetrieveUpdateDestroyView,
                    VehicleAccessoriesListCreateView, VehicleAccessoriesRetrieveUpdateDestroyView,
                    ReviewListCreateView, ReviewRetrieveUpdateDestroyView, GetOrCreatePropertyCardView,
                    UserListCreateAPIView)

urlpatterns = [
    path("users/", UserListCreateAPIView.as_view(), name='users'),
    path('persons/', PersonListAPIView.as_view(), name='persons'),
    path('property-cards/', PropertyCardAPIView.as_view(), name='property-cards'),
    path('vehicle/', VehicleAPIView.as_view(), name='vehicle'),
    path('vehicle-engines/', VehicleEngineListCreateView.as_view(), name='vehicle-engine-list-create'),
    path('vehicle-engines/<int:pk>/', VehicleEngineRetrieveUpdateDestroyView.as_view(), name='vehicle-engine-detail'),
    path('vehicle-accessories/', VehicleAccessoriesListCreateView.as_view(), name='vehicle-accessories-list-create'),
    path('vehicle-accessories/<int:pk>/', VehicleAccessoriesRetrieveUpdateDestroyView.as_view(), name='vehicle-accessories-detail'),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail'),
    path('read-property-card/', GetOrCreatePropertyCardView.as_view(), name='review-detail'),
]
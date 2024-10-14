from django.urls import path

from .views import PersonListAPIView,PropertyCardAPIView

urlpatterns = [
    path('persons/', PersonListAPIView.as_view(), name='persons'),
    path('property-cards/', PropertyCardAPIView.as_view(), name='property-cards'),
]
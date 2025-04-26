from django.urls import path, include
from rest_framework import routers

from .views import CountryListCreateAPIView, CountryRetrieveUpdateDestroyAPIView, ManufacturerViewSet

router = routers.SimpleRouter()
router.register(r'manufacturers', ManufacturerViewSet, basename='manufacturers')

urlpatterns = [
    path('', include(router.urls)),
    path('countries/', CountryListCreateAPIView.as_view(), name='country-list-create'),
    path('countries/<int:pk>/', CountryRetrieveUpdateDestroyAPIView.as_view(), name='country-detail'),
]

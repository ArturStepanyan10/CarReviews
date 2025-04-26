from django.urls import path, include
from rest_framework import routers

from .views import CountryListCreateAPIView, CountryRetrieveUpdateDestroyAPIView, ManufacturerViewSet, CarViewSet, \
    CommentViewSet

router = routers.SimpleRouter()
router.register(r'manufacturers', ManufacturerViewSet, basename='manufacturers')
router.register(r"cars", CarViewSet, basename='cars')
router.register(r"comment", CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('countries/', CountryListCreateAPIView.as_view(), name='country-list-create'),
    path('countries/<int:pk>/', CountryRetrieveUpdateDestroyAPIView.as_view(), name='country-detail'),
]

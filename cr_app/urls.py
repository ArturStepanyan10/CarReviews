from django.urls import path, include
from rest_framework import routers

from .views import CountryListCreateAPIView, CountryRetrieveUpdateDestroyAPIView, ManufacturerViewSet, CarViewSet, \
    CommentViewSet, export_cars

router = routers.SimpleRouter()
router.register(r'manufacturers', ManufacturerViewSet, basename='manufacturers')
router.register(r"cars", CarViewSet, basename='cars')
router.register(r"comments", CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('countries/', CountryListCreateAPIView.as_view(), name='country-list-create'),
    path('countries/<int:pk>/', CountryRetrieveUpdateDestroyAPIView.as_view(), name='country-detail'),
    path('export-cars/', export_cars, name='export-cars'),
]

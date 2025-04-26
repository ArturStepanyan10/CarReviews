from django.urls import path

from .views import CountryListCreateAPIView, CountryRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('countries/', CountryListCreateAPIView.as_view(), name='country-list-create'),
    path('countries/<int:pk>/', CountryRetrieveUpdateDestroyAPIView.as_view(), name='country-detail'),
]

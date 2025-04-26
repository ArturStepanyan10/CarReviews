from rest_framework import serializers

from cr_app.models import Country, Manufacturer, Car


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'country_id']


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ['id', 'name',]


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'name', 'release_year', 'graduation_year', 'manufacturer_id']

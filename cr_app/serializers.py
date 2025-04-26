from rest_framework import serializers

from cr_app.models import Country, Manufacturer, Car, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'email', 'content', 'car_id', 'created_at']

    def validate_content(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('Комментарий должен содержать минимум 10 символов.')
        return value


class CarSerializer(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField()
    manufacturer = serializers.StringRelatedField(source='manufacturer_id', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'name', 'release_year', 'graduation_year', 'manufacturer_id', 'manufacturer', 'comments_count', 'comments']

    def get_comments_count(self, obj):
        return obj.cars.count()


class ManufacturerSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField(source='country_id', read_only=True)
    cars = CarSerializer(source='manufacturers', many=True, read_only=True)

    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'country_id', 'country', 'cars']


class CountrySerializer(serializers.ModelSerializer):
    manufacturers = ManufacturerSerializer(source='countries', many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'name', 'manufacturers']






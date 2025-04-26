import csv
from io import BytesIO

import openpyxl
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from cr_app.models import Country, Manufacturer, Car, Comment
from cr_app.serializers import CountrySerializer, ManufacturerSerializer, CarSerializer, CommentSerializer


class CountryListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CountryRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        country = get_object_or_404(Country, pk=pk)
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    def put(self, request, pk):
        country = get_object_or_404(Country, pk=pk)
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        country = get_object_or_404(Country, pk=pk)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsAuthenticated]


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
def export_cars(request):
    export_format = request.GET.get('form')

    cars = Car.objects.select_related('manufacturer_id')

    if export_format == 'xlsx':

        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(['ID', 'Name', 'Manufacturer', 'Release year', 'Graduation year'])

        for car in cars:
            ws.append([car.id, car.name, car.manufacturer_id.name, car.release_year, car.graduation_year])

        file_stream = BytesIO()
        wb.save(file_stream)
        file_stream.seek(0)

        response = HttpResponse(
            file_stream.read(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )
        response['Content-Disposition'] = 'attachment; filename="cars.xlsx"'
        return response

    elif export_format == 'csv':

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="cars.csv"'

        writer = csv.writer(response)
        writer.writerow(['ID', 'Name', 'Manufacturer', 'Release year', 'Graduation year'])

        for car in cars:
            writer.writerow([car.id, car.name, car.manufacturer_id.name, car.release_year, car.graduation_year])

        return response

    else:
        response = HttpResponse("К сожалению, в другие форматы экспорт не предусматривается!")
        return response


class CommentViewSet(
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['list', 'create']:
            return [AllowAny()]
        return [IsAuthenticated()]

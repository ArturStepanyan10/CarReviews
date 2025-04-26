from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False, verbose_name='Название')

    def __str__(self):
        return f"{self.name}"


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False,
                            verbose_name='Название')
    country_id = models.ForeignKey(Country, null=False, blank=False,
                                   on_delete=models.CASCADE, related_name='countries', verbose_name='Страна')

    def __str__(self):
        return f"{self.name}"


class Car(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    release_year = models.IntegerField(null=False, blank=False, verbose_name='Год начала выпуска')
    graduation_year = models.IntegerField(null=False, blank=False, verbose_name='Год окончания выпуска')
    manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='manufacturers',
                                        verbose_name='Производитель')

    def __str__(self):
        return f"{self.name}"


class Comment(models.Model):
    email = models.EmailField(max_length=255, null=False, blank=False, unique=True, verbose_name='Email')
    content = models.TextField(null=False, blank=False, verbose_name='Комментарий')
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='cars', verbose_name='Автомобиль')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.email} -> {self.content[:15]}"

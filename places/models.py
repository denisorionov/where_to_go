from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    id = models.AutoField('№', primary_key=True)
    title = models.CharField('Название', max_length=100)
    description_short = models.CharField('Краткое описание', max_length=400, blank=True)
    description_long = tinymce_models.HTMLField('Описание', blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    class Meta:
        verbose_name_plural = 'Локации'  # название модели в множественном числе

    def __str__(self):
        return self.title


class Image(models.Model):
    id = models.AutoField('№', primary_key=True)
    position = models.PositiveIntegerField('Позиция', default=0, null=True, blank=True)
    img = models.ImageField('Фото', upload_to='picture')
    place = models.ForeignKey(Place, verbose_name='Локация', on_delete=models.CASCADE, related_name='images', blank=True)

    class Meta:
        verbose_name_plural = 'Фото'
        ordering = ['position']

    def __str__(self):
        return self.place.title

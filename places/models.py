from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField('Название', max_length=100)
    short_description = models.TextField('Краткое описание', blank=True)
    long_description = tinymce_models.HTMLField('Описание', blank=True)
    lng = models.FloatField('Долгота', db_index=True)
    lat = models.FloatField('Широта', db_index=True)

    class Meta:
        verbose_name_plural = 'Локации'  # название модели в множественном числе

    def __str__(self):
        return self.title


class Image(models.Model):
    position = models.PositiveIntegerField('Позиция', default=0, null=True, blank=True, db_index=True)
    img = models.ImageField('Фото', upload_to='picture')
    place = models.ForeignKey(Place, verbose_name='Локация', on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name_plural = 'Фото'
        ordering = ['position']

    def __str__(self):
        return self.place.title

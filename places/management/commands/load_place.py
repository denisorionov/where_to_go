#  комманда для загрузки новых локаций из json файлов

from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('link', nargs='+', type=str)

    def handle(self, *args, **options):
        for link in options['link']:
            r = requests.get(link)
            data = r.json()
            new_place = Place.objects.create(title=data['title'],
                                             description_short='description_short',
                                             description_long=data['description_long'],
                                             lng=data['coordinates']['lng'],
                                             lat=data['coordinates']['lat'])
            for img_url in data['imgs']:
                name = urlparse(img_url).path.split('/')[-1]
                img_content = ContentFile(requests.get(img_url).content)
                new_img = Image(place=new_place)
                new_img.img.save(name, img_content, save=True)
                new_img.save()

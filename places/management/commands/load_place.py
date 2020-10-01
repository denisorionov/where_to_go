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
            r.raise_for_status()
            json_file = r.json()
            new_place, created = Place.objects.get_or_create(title=json_file['title'],
                                                             short_description=json_file['description_short'],
                                                             long_description=json_file['description_long'],
                                                             lng=json_file['coordinates']['lng'],
                                                             lat=json_file['coordinates']['lat'])
            for img_url in json_file['imgs']:
                name = urlparse(img_url).path.split('/')[-1]
                requests.get(img_url).raise_for_status()
                img_content = ContentFile(requests.get(img_url).content)
                new_img = Image(place=new_place)
                new_img.img.save(name, img_content, save=True)
                new_img.save()

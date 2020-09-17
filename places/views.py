from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View

from places.models import Place, Image


class MainView(View):  # главная страница
    def get(self, request):
        features = []

        for place in Place.objects.all():
            features.append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse('place_json', args=[place.id]),
                }
            })

        geojson = {
            "type": "FeatureCollection",
            "features": features
        }

        return render(request, 'index.html', context={'geojson': geojson})


class PlaceJsonView(View):  # страница с json файлом
    def get(self, request, num):
        place = get_object_or_404(Place, pk=num)
        imgs = []

        for img in place.images.all():
            imgs.append(img.img.url)

        data = {
            'title': place.title,
            'imgs': imgs,
            'description_short': place.short_description,
            'description_long': place.long_description,
            'coordinates': {
                'lng': place.lng,
                'lat': place.lat
            }
        }

        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from places.views import MainView, PlaceJsonView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),  # главная страница
    path('place/<int:number>', PlaceJsonView.as_view(), name='place_json')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

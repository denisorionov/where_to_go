from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    def preview(self, obj):
        if obj.img:
            return format_html('<img src="{}" height="200"/>', obj.img.url)
        else:
            return ("Здесь будет превью, когда вы выберете файл.")

    readonly_fields = ['preview']
    model = Image
    extra = 0


class PlaceAdmin(admin.ModelAdmin):
    indexCnt = 0

    def index_counter(self, obj):  # нумерация строк list_display
        count = Place.objects.all().count()
        if self.indexCnt < count:
            self.indexCnt += 1
        else:
            self.indexCnt = 1
        return self.indexCnt

    index_counter.short_description = "№"

    inlines = [ImageInline]
    list_display = ['index_counter', 'title', 'short_description']
    list_display_links = ['title']  # сылка для редактирования
    search_fields = ['title']
    ordering = ['id']


admin.site.register(Place, PlaceAdmin)

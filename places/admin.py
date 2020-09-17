from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Image


class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    def preview(self, obj):
        return format_html('<img src="{url}" height="200" />'.format(url=obj.img.url))

    readonly_fields = ['preview']
    list_display = ('position', 'place', 'preview')


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    def preview(self, obj):
        return format_html('<img src="{}" height="200"/>', obj.img.url)

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

    inlines = (ImageInline,)
    list_display = ('index_counter', 'title', 'short_description')
    list_display_links = ('title',)  # сылка для редактирования
    search_fields = ['title']
    ordering = ('id',)


admin.site.register(Place, PlaceAdmin)

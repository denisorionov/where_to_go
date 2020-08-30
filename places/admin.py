from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
from places.models import Place, Image


class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    def preview(self, obj):
        return format_html('<img src="{url}" height="200" />'.format(url=obj.img.url))

    readonly_fields = ['preview']
    list_display = ('position', 'place',  'preview')


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    def preview(self, obj):
        return format_html('<img src="{url}" height="200"/>'.format(url=obj.img.url))

    readonly_fields = ['preview']
    model = Image
    extra = 0


class PlaceAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)
    list_display = ('id', 'title', 'description_short')
    search_fields = ['title']
    ordering = ('id', )


admin.site.register(Place, PlaceAdmin)
# admin.site.register(Image, ImageAdmin)

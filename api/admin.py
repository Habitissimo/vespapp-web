from django.contrib import admin

from api.models import *


class ImageAdmin(admin.ModelAdmin):
    list_display = ['image_tag']

class ImageInline(admin.TabularInline):
    model = Picture

class SightingAdmin(admin.ModelAdmin):
    list_display = ('location', 'href_location_tag')
    inlines = [ImageInline ]


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Sighting, SightingAdmin)
admin.site.register(Picture)
admin.site.register(UserComment)
admin.site.register(ExpertComment)
admin.site.register(SightingFAQ)

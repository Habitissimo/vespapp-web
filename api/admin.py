from django.contrib import admin

from api.models import *

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Sighting)
admin.site.register(Picture)
admin.site.register(UserComment)
admin.site.register(ExpertComment)

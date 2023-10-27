from django.contrib import admin
from api.markers.models import Marker


class MarkersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


admin.site.register(Marker, MarkersAdmin)

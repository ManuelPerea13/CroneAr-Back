from django.contrib import admin
from api.markers.models import Marker, UserMarker


class MarkersAdmin(admin.ModelAdmin):
    list_display = ('id', 'marker_name', 'user', )


admin.site.register(Marker, MarkersAdmin)
admin.site.register(UserMarker)

from django.contrib import admin
from api.users.models import CustomUser


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')


admin.site.register(CustomUser, UsersAdmin)

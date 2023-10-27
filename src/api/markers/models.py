from django.db import models

from api.users.models import CustomUser


class Marker(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                             related_name='markers')
    name = models.CharField(max_length=45, null=True)
    brand = models.CharField(max_length=45, null=True)
    model = models.CharField(max_length=45, null=True)
    serial_number = models.CharField(max_length=45, null=True)
    details = models.CharField(max_length=45, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%i: %s' % (
            self.pk,
            self.user
        )

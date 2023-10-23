from django.db import models


class Marker(models.Model):
    marker_name = models.CharField(max_length=45, null=True)
    brand_name = models.CharField(max_length=45, null=True)
    standard = models.IntegerField(default=1)
    date_add = models.DateTimeField(null=True)
    date_mod = models.DateTimeField(null=True)
    id_role = models.PositiveIntegerField()
    fuckingmorfology = models.CharField(max_length=45, null=True)
    details = models.CharField(max_length=45, null=True)
    hidden = models.IntegerField(default=0, null=True)
    fps = models.IntegerField(null=True)
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='markers')

    def __str__(self):
        return '%i: %s' % (
            self.pk,
            self.marker_name
        )


class UserMarker(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    marker = models.ForeignKey(Marker, on_delete=models.CASCADE)
    date_add = models.DateTimeField(null=True)
    date_mod = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.pk} {self.user} - {self.marker}'

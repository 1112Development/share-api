import uuid

from django.db import models
from django.utils.datetime_safe import datetime


class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lat = models.FloatField(max_length=255, blank=False, null=False)
    long = models.FloatField(max_length=255, blank=False, null=False)
    original = models.ImageField(max_length=1000, blank=False, null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(max_length=1000, blank=False, null=False)
    created = models.DateTimeField(editable=False)

    def save(self, **kwargs):
        if not self.created:
            self.created = datetime.now()
        super(Photo, self).save()

    def self_destruct(self):
        """Determine if photo should be deleted"""
        pass

    def make_thumbnail(self):
        """Automaticlly create thumbnail of self"""
        pass

    def location(self):
        """Return latitude and longitude Tuple"""
        return self.lat, self.lng

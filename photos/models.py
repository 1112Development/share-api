import cloudinary as cloudinary
from cloudinary.models import CloudinaryField
from django.db import models
from django.utils.datetime_safe import datetime
import cloudinary.api


class Photo(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    lat = models.FloatField(max_length=255, blank=False, null=False)
    long = models.FloatField(max_length=255, blank=False, null=False)
    created = models.DateTimeField(editable=False)
    original = CloudinaryField('original')

    def save(self, **kwargs):
        if not self.created:
            self.created = datetime.now()
            self.id = self.original.public_id
        super(Photo, self).save()

    def self_destruct(self):
        """Determine if photo should be deleted"""
        pass

    def location(self):
        """Return latitude and longitude Tuple"""
        return self.lat, self.long

    def delete(self, using=None, keep_parents=False):
        cloudinary.api.delete_resources(public_ids=[self.original.public_id])
        return super(Photo, self).delete()

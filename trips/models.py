# trips/models.py

from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    location_data = models.CharField(max_length=100)
    weather = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class GisPoint(models.Model):
    lat = models.CharField(max_length=20)
    lon = models.CharField(max_length=20)
    item = models.CharField(max_length=100)




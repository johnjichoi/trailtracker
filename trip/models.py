from django.db import models
from django.contrib.auth import get_user_model

class Trip(models.Model):
    trip_name = models.CharField(max_length=50)
    trip_date = models.DateField()
    location = models.CharField(max_length=50)
    distance_kilometre = models.IntegerField(blank=True, null=True)
    duration_hour = models.IntegerField(blank=True, null=True)
    elevation_gain_metre = models.IntegerField(blank=True, null=True)
    elevation_loss_metre = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

class UserTrip(models.Model):
    user = models.ForeignKey(
        get_user_model(), 
        null=True,
        on_delete=models.CASCADE
    )
    trip = models.ForeignKey(
        Trip, 
        null=True,
        on_delete=models.CASCADE
    )

class TripPhoto(models.Model):
    trip = models.ForeignKey(
        Trip, 
        null=True,
        on_delete=models.CASCADE
    )
    photo = models.FileField(upload_to='trip/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

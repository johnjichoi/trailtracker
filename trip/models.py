from django.db import models
from django.contrib.auth import get_user_model

class Trip(models.Model):
    trip_name = models.CharField(max_length=50)
    trip_date = models.DateField()
    location = models.CharField(max_length=50)
    distance_metre = models.IntegerField()
    duration_second = models.IntegerField()
    elevation_gain_metre = models.IntegerField()
    elevation_loss_metre = models.IntegerField()
    note = models.TextField()

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

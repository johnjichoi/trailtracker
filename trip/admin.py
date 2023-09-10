from django.contrib import admin

from .models import (
    Trip,
    TripPhoto,
    UserTrip
)

# Register your models here.
admin.site.register(Trip)
admin.site.register(TripPhoto),
admin.site.register(UserTrip)
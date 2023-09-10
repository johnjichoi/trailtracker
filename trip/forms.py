from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Trip, TripPhoto

class TripForm(forms.ModelForm):
	class Meta:
		model = Trip
		fields = (
			'trip_name',
			'trip_date',
			'location',
			'distance_kilometre',
			'duration_hour',
			'elevation_gain_metre',
			'elevation_loss_metre',
			'note',
		)
		widgets = {
            'note': forms.Textarea(attrs={"cols": 80, "rows": 20}),
        }
		labels = {
			'trip_name': _('Name'),
			'trip_date': _('Date'),
			'location': _('Location'),
			'distance_kilometre': _('Distance (KM)'),
			'duration_hour': _('Duration (Hour)'),
			'elevation_gain_metre': _('Elevation Gain (M)'),
			'elevation_loss_metre': _('Elevation Loss (M)'),
			'note': _('Notes'),
        }

class TripPhotoForm(forms.ModelForm):
    class Meta:
        model = TripPhoto
        exclude = ('trip', 'uploaded_at')
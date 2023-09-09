from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Trip
from .tables import TripTable

@login_required
def homepage_request(request):
	table = TripTable(Trip.objects.all())

	return render(
		request=request, 
		template_name='trip.html',
		context={'table': table}
	)

@login_required
def add_request(request):
	return render(
		request=request, 
		template_name='add.html'
	)

@login_required
def edit_request(request):
	return render(
		request=request, 
		template_name='edit.html',
	)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    redirect,
    render
)
from django_tables2 import RequestConfig

from .forms import (
    TripForm,
    TripPhotoForm
)
from .models import (
    Trip,
    TripPhoto,
    UserTrip
)
from .tables import TripTable

@login_required
def add_request(request):
    if request.method != 'POST':
        form = TripForm()

        return render(
            request = request,
            template_name = 'add.html',
            context = {'trip_form': form}
        )
    
    form = TripForm(request.POST)

    if not form.is_valid():
        messages.error(request, 'Failed to add trip')
        return render(
            request=request, 
            template_name='add.html', 
            context={'trip_form':form}
        )

    trip = form.save()

    user_trip = UserTrip(
        user=request.user,
        trip=trip
    )
    user_trip.save()

    messages.success(request, 'Added trip')
    return redirect('trip:trip')

@login_required
def delete_request(request, id):
    trip = Trip.objects.get(pk=id)
    if not trip:
        messages.error(request, 'Invalid trip')
        return redirect('trip:trip')
    
    if request.method != 'POST':
        return render(
            request=request, 
            template_name='delete.html',
            context={'trip':trip}
        )
    
    trip.delete()
    messages.success(request, 'Deleted trip')
    return redirect('trip:trip')

@login_required
def edit_request(request, id):
    trip = Trip.objects.get(pk=id)
    if not trip:
        messages.error(request, 'Invalid trip')
        return redirect('trip:trip')
        
    if request.method != 'POST':
        form = TripForm(instance=trip)

        return render(
            request=request, 
            template_name='edit.html',
            context={'trip_form':form}
        )
    
    form = TripForm(request.POST, instance=trip)
    if not form.is_valid():
        messages.error(request, 'Failed to edit trip')
        return render(
            request=request, 
            template_name='edit.html', 
            context={'trip_form':form}
        )
    
    form.save()

    messages.success(request, 'Trip edited')
    return redirect('trip:trip')

@login_required
def trip_request(request):
    current_user = request.user

    user_trip = UserTrip.objects.filter(user=current_user)
    
    table = TripTable(Trip.objects.filter(
        pk__in=user_trip.values_list('trip', flat=True)
    ))

    RequestConfig(request).configure(table)

    table.paginate(
        page=request.GET.get('page', 1), 
        per_page=5
    )

    return render(
        request=request, 
        template_name='trip.html',
        context={'table': table}
    )

@login_required
def upload_request(request, id):
    trip = Trip.objects.get(pk=id)
    if not trip:
        messages.error(request, 'Invalid trip')
        return redirect('trip:trip')

    if request.method == 'POST':
        form = TripPhotoForm(
            data=request.POST, 
            files=request.FILES
        )
        if not form.is_valid():
            messages.error(request, 'Failed to upload photo')
            return render(
                request=request, 
                template_name='upload.html',
                context={'form': form}
            )

        trip_photo = form.save(commit=False)
        trip_photo.trip = trip
        trip_photo.save()

        messages.success(request, 'Uploaded photo')
        return redirect('trip:trip')

    form = TripPhotoForm()
    return render(
        request=request, 
        template_name='upload.html',
        context={'photo_form': form}
    )

@login_required
def view_request(request, id):
    trip = Trip.objects.get(pk=id)
    if not trip:
        messages.error(request, 'Invalid trip')
        return redirect('trip:trip')
    
    trip_photo = TripPhoto.objects.filter(trip__id=trip.id)
    # debug
    print(trip_photo.values())
    
    return render(
        request=request, 
        template_name='view.html',
        context={
            'trip': trip,
            'photo': trip_photo
        }
    )

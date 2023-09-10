from django_tables2 import Table, TemplateColumn
from django.utils.translation import gettext_lazy as _
from .models import Trip

class TripTable(Table):
    upload = TemplateColumn('''
        <a href="/trip/{{record.id}}/upload" class="btn btn-primary">Upload Photo</a>
    ''', verbose_name='') 
    action = TemplateColumn('''
        <a href="/trip/{{record.id}}/view" class="btn btn-primary">View</a>
        <a href="/trip/{{record.id}}/edit" class="btn btn-primary">Edit</a>
        <a href="/trip/{{record.id}}/delete" class="btn btn-danger">Delete</a>
    ''', verbose_name='')      

    class Meta:
        model = Trip
        fields = ['trip_name', 'trip_date', 'location', 'distance_kilometre']
        labels = {
            'trip_name': _('Name'),
            'trip_date': _('Date'),
            'location': _('Location'),
            'distance_kilometre': _('Distance'),
        }
        attrs = {'class': 'table table-striped'}

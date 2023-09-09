from django_tables2 import Table, TemplateColumn
from .models import Trip

class TripTable(Table):
    class Meta:
        model = Trip
        attrs = {'class': 'table table-sm'}

    edit = TemplateColumn(template_name='trips_edit.html')
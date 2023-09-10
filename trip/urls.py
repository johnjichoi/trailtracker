from django.urls import path
from . import views

app_name = 'trip'

urlpatterns = [
    path('', views.trip_request, name='trip'),
    path('add', views.add_request, name='add'),
    path('<int:id>/delete', views.delete_request, name='delete'),
    path('<int:id>/edit', views.edit_request, name='edit'),
    path('<int:id>/view', views.view_request, name='view'),
]

from django.urls import path
from . import views

app_name = 'trip'

urlpatterns = [
    path('', views.homepage_request, name='homepage'),
    path('add', views.add_request, name='add'),
    path('edit', views.edit_request, name='edit'),
]

from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homepage_request, name='homepage'),
    path('login', views.login_request, name='login'),
    path("logout", views.logout_request, name= "logout"),
    path('register', views.register_request, name='register'),
    path('trails', views.trails_request, name='trails'),
]
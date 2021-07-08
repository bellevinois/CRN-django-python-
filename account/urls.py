from django.urls import path
from . import views


urlpatterns = [

    path('Registration', views.registrationPage, name='Registration'),
    path('acces', views.accesPage, name='acces'),
]
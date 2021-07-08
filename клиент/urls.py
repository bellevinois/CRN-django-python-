from django.urls import path
from . import views

urlpatterns = [

    path('<str:pk>',views.list_clients,name='client'),
    path('ajout_clients/', views.ajouter_clients, name='ajout_clients'),
]
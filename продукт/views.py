from django.shortcuts import render
from django.http import HttpResponse
from клиент.models import Client
from заказ.models import Commande

# Create your views here.
def home(request):
    commandes = Commande.objects.all()
    clients = Client.objects.all()
    context = {'commandes':commandes,
               'clients': clients}
    return render(request,'продукт/home.html',context)
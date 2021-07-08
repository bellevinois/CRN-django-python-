from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ClientForm
from .models import Client

# Create your views here.
def list_clients(request, pk):
    client=Client.objects.get(id=pk)
    commande=client.commande_set.all()
    commande_totale=commande.count()
    context={'client': client,
             'commande':commande,
             'commande_totale':commande_totale}
    return render(request,'клиент/список_клиентов.html',context)

def ajouter_clients(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    contex ={'form':form}
    return render(request,'клиент/liste_clients.html',contex)
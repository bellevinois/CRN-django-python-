from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CommandeForm
from .models import Commande

# Create your views here.
def list_commandes(request):
    return render(request,'заказ/Список_заказов.html')

def ajouter_commande(request):
    form = CommandeForm()
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    contex ={'form':form}
    return render(request,'заказ/ajouter_commande.html',contex)

def modifier_commande(request,pk):
    commande = Commande.objects.get(id=pk)
    form = CommandeForm(instance = commande)
    if request.method == 'POST':
        form = CommandeForm(request.POST, instance = commande)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'заказ/ajouter_commande.html', context)

def supprimer_commande(request,pk):
    commande = Commande.objects.get(id=pk)
    if request.method == 'POST':
        commande.delete()
        return redirect('/')
    context = {'items': commande}
    return render(request,'заказ/supprimer.html',context)
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .form import newUser

# Create your views here.
def registrationPage(request):
    form = newUser()
    if request.method == 'POST':
        form = newUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'аккаунт сщздан успешно для ' + user)
            return redirect('home')
    context = {'form':form}
    return render(request, 'account/Registration.html', context)

def accesPage(request):
    context = {}
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, "логин или пароль не верен")
    return render(request, 'account/acces.html', context)
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def home(request):
    return render(request, 'home.html')


def SignUp(request):

    if request.method == 'GET':
        return render(request, 'signUp.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Register User
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user) #Guarda los datos de sesión a la cookie de la página
                return redirect('inventory')
            except IntegrityError:
                return render(request, 'signUp.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'signUp.html', {
            'form': UserCreationForm,
            'error': 'Contraseñas no coinciden'
        })


def inventory(request):
    return render(request, 'inventory.html')

def signout(request):
    logout(request)
    return redirect('login')

def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña son incorrectas. Verifíque sus datos'
            })
        else:
            login(request, user)
            return redirect('inventory')

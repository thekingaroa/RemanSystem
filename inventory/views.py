from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

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
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return HttpResponse('Usuario creado correctamente')
           except:
               return HttpResponse('el usuario ya existe')
        return HttpResponse('Las contraseñas no coinciden')
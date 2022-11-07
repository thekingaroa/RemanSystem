from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def HelloWorld(request):
    return render(request, 'signUp.html', {
        'form': UserCreationForm
    })
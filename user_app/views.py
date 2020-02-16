from django.shortcuts import render
from . import forms

# Create your views here.

def index(request):
    return render(request,'user_app/index.html')

def sign_up(request):
    form = forms.User_Form()
    return render(request, 'user_app/sign_up.html', {'form':form})

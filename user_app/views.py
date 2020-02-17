from django.shortcuts import render
#from . import forms
from user_app.forms import User_Form

# Create your views here.

def index(request):
    return render(request,'user_app/index.html')

def sign_up(request):


    #form = forms.User_Form()
    form = User_Form()
    if request.method == 'POST':
        form = User_Form(request.POST)

        if form.is_valid():
            form.save()
            return index(request)
        else:
            print('error in view.py user_app')
    return render(request, 'user_app/sign_up.html', {'form':form})

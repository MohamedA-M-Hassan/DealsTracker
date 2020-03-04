from django.shortcuts import render
#from . import forms
from user_app.forms import User_Form,UserProfileInfoForm

# Login Import
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'user_app/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    #return HttpResponseRedirect('user_app/index')
    return render(request,'user_app/index.html')

def sign_up(request):

    registered = False

    ##form = User_Form()
    if request.method == 'POST':
        user_form = User_Form(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit =False)
            profile.user = user

            if 'profile_pic' is request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()
            registered= True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = User_Form()
        profile_form = UserProfileInfoForm()


    return render(request, 'user_app/sign_up.html',
                    {'user_form':user_form, 'profile_form':profile_form,'registered':registered})




def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("someone tried to login and failed")
            print("Username:{} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")

    else:
        return render(request, 'user_app/login.html',{})

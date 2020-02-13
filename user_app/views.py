from django.shortcuts import render

# Create your views here.

def sign_up(request):
    return render(request, 'user_app/sign_uP.html', {})

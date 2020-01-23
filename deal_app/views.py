from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    ##return HttpResponse("<em>Hello World!</em>")
    my_dic ={'insert_me':2+3   }
    return render(request, 'deal_app/index.html', context=my_dic)

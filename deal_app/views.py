from django.shortcuts import render
from django.http import HttpResponse
from deal_app.models import Customer, Deal

# Create your views here.

def index(request):
    ##return HttpResponse("<em>Hello World!</em>")
    #my_dic ={'insert_me':2+3   }
    deals = Deal.objects.all()
    deals_dictionary = {'deals': deals}
    return render(request, 'deal_app/index.html', context=deals_dictionary)



def main(request):
    return render(request,'deal_app/main.html')

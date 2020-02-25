from django.shortcuts import render
from django.http import HttpResponse
from deal_app.models import Customer, Deal
from deal_app.forms import Deal_Form

# Create your views here.

def index(request):
    ##return HttpResponse("<em>Hello World!</em>")
    #my_dic ={'insert_me':2+3   }
    deals = Deal.objects.all()
    deals_dictionary = {'deals': deals}
    return render(request, 'deal_app/index.html', context=deals_dictionary)



def main(request):
    deals = Deal.objects.all()
    deals_dictionary = {'deals': deals}
    return render(request,'deal_app/main.html', context=deals_dictionary)


def booky(request):
    return render(request,'deal_app/booky.html')





def new_deal(request):

    #form = forms.User_Form()
    form = Deal_Form()
    if request.method == 'POST':
        form = Deal_Form(request.POST)

        if form.is_valid():
            form.save()
            return main(request)
        else:
            print('error in view.py deal_app')
    return render(request, 'deal_app/add_new_deal.html', {'form':form})

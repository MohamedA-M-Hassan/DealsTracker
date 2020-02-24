from deal_app import views
from django.conf.urls import url


app_name = 'deal_app'
urlpatterns=[
    url(r'^main/',views.main,name='main'),
    url(r'^booky/',views.booky,name='booky'),
    url(r'^new_deal/',views.new_deal,name='new_deal'),
]

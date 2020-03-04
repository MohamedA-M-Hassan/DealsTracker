from deal_app import views
from django.conf.urls import url


app_name = 'deal_app'
urlpatterns=[
    url(r'^main/',views.main,name='main'),
    url(r'^new_deal/',views.new_deal,name='new_deal'),
    url(r'^customers/',views.customers,name='customers'),
    url(r'^customers_submission/',views.customer_submit_his_deal,name='customers_submission'),
]

from deal_app import views
from django.conf.urls import url


app_name = 'deal_app'
urlpatterns=[
    url(r'',views.index,name='index'),
    url(r'^main/',views.main,name='main'),
]

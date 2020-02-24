from user_app import views
from django.conf.urls import url

app_name = 'user_app'

urlpatterns=[
    url(r'^sign_up/',views.sign_up,name='sign_up'),
    url(r'^index/',views.index,name='index'),

    #url(r'other/',views.other,name='other')
]

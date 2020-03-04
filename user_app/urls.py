from user_app import views
from django.conf.urls import url

app_name = 'user_app'

urlpatterns=[
    url(r'^sign_up/',views.sign_up,name='sign_up'),
    url(r'^index/',views.index,name='index'),
    url(r'^user_login/',views.user_login,name='user_login')
    #url(r'other/',views.other,name='other')
]

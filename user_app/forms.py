from django import forms
from django.contrib.auth.models import User
from user_app.models import UserProfileInfo



from user_app.models import User


class User_Form(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
#    name = forms.CharField()
#    email = forms.EmailField()
#    password = forms.CharField()
#    phone = forms.CharField()

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')


    #text = forms.CharField(widget = forms.Textarea)

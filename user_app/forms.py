from django import forms
from user_app.models import User


class User_Form(forms.ModelForm):

#    name = forms.CharField()
#    email = forms.EmailField()
#    password = forms.CharField()
#    phone = forms.CharField()

    class Meta():
        model = User
        fields = '__all__'

    #text = forms.CharField(widget = forms.Textarea)

from django import forms
from deal_app.models import Deal


class Deal_Form(forms.ModelForm):

    class Meta():
        model = Deal
        fields = '__all__'

    #text = forms.CharField(widget = forms.Textarea)

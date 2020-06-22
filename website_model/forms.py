from django import forms
from website_model.models import Member,ordr
from django.forms import ModelForm
class Membr_form(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = Member
        fields=('__all__')

class ord_form(ModelForm):
    class Meta():
        model=ordr
        fields=('__all__')

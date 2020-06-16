from app.models import *
#from django.contrib.auth.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class UserCreationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=Registration
        fields='__all__'

class LoginForm(forms.ModelForm):
    class Meta:
        model=Registration
        fields=['email','password']


class InvestorForm(forms.ModelForm):
    class Meta:
        model= Investor
        fields='__all__'

class MoneyFinderForm(forms.ModelForm):
    class Meta:
        model= MoneyFinder
        fields= '__all__'

class OthersForm(forms.ModelForm):
    class Meta:
        model=Others
        fields='__all__'










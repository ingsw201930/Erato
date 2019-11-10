from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TransactionForm(forms.Form):
    name = forms.CharField(label='Name', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    last_name = forms.CharField(label='Last name', max_length=20,
                               widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    address = forms.CharField(label='Address', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Address'}))

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DateAddForm(forms.Form):
    start_time  = forms.DateTimeField( widget=forms.TextInput(attrs={'placeholder': 'Start time'}))
    end_time = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'Finish time'}))
    lng       = forms.DecimalField(label='longitude', widget=forms.TextInput(attrs={'type': 'hidden'}))
    lat       = forms.DecimalField(label='latitude', widget=forms.TextInput(attrs={'type': 'hidden'}))

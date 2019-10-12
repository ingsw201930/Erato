from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DateAddForm(forms.Form):
    start_time  = forms.CharField( label='s_date', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Start date'}))
    end_time = forms.CharField(label='e_date', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Finish date'}))
    start_time_hms  = forms.CharField( label='s_time', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Start time'}))
    end_time_hms = forms.CharField(label='e_time', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Finish time'}))
    lng       = forms.DecimalField(label='longitude', widget=forms.TextInput(attrs={'type': 'hidden'}))
    lat       = forms.DecimalField(label='latitude', widget=forms.TextInput(attrs={'type': 'hidden'}))

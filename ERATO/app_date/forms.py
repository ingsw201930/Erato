from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DateAddForm(forms.Form):
    start_time  = forms.DateTimeField()
    finish_time = forms.DateTimeField()
    place       = forms.CharField(label='Place', max_length=200)


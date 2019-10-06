from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ServiceAddForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    description = forms.CharField(label='Description', max_length=500)
    price = forms.IntegerField(label='Price',max_value=10000000)


class SWSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.')
    third_email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.')
    birthDate=forms.DateTimeField()
    description=forms.CharField(max_length=500)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2'
        ,'description' )

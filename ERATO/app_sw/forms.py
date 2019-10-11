from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UploadFileForm(forms.Form):
    file = forms.ImageField()

class ServiceAddForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    description = forms.CharField(label='Description', max_length=500, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    price = forms.IntegerField(label='Price',max_value=100000, widget=forms.TextInput(attrs={'placeholder': 'Price'}))


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

class ServiceFilterForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
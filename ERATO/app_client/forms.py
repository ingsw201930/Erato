from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UploadFileForm(forms.Form):
    file = forms.ImageField(widget=forms.FileInput(attrs={'class': 'ui primary button', 'style':'display: block', 'onchange':'loadImage(event)'}))

class UploadMCForm(forms.Form):
    mc = forms.FileField(widget=forms.FileInput(attrs={'class': 'ui primary button', 'style':'display: block', 'onchange':'loadFile(event)'}))

class ClientSignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'validate','placeholder': 'Username', 'style':'margin-bottom: 10px;'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Type your password', 'style':'margin-bottom: 10px;'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Type again your password', 'style':'margin-bottom: 10px;'}))
    #first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'First name', 'style':'margin-bottom: 10px;'}))
    #last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Last name', 'style':'margin-bottom: 10px;'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', widget=forms.TextInput(attrs={'placeholder': 'Email', 'style':'margin-bottom: 10px;'}))
    #birth_date=forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'Birth date'}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email' )

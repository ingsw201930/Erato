from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_sw.forms import Tag

class UploadFileForm(forms.Form):
    file = forms.ImageField(widget=forms.FileInput(attrs={'class': 'ui primary button', 'style':'display: none', 'onchange':'loadImage(event)'}))

class UploadMCForm(forms.Form):
    mc = forms.FileField(widget=forms.FileInput(attrs={'class': 'ui primary button', 'style':'display: none', 'onchange':'loadFile(event)'}))

class ClientSignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'validate','placeholder': 'Username', 'style':'margin-bottom: 10px;'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Type your password', 'style':'margin-bottom: 10px;'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Type again your password', 'style':'margin-bottom: 10px;'}))
    about = forms.CharField(max_length=280, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Acerca de mí', 'style':'margin-bottom: 10px;'}))
    birth_date=forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'Birth date'}))
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'First name', 'style':'margin-bottom: 10px;'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Last name', 'style':'margin-bottom: 10px;'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', widget=forms.TextInput(attrs={'placeholder': 'Email', 'style':'margin-bottom: 10px;'}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email' )

class ClientEditForm(forms.Form):
    email = forms.EmailField(max_length=80, help_text='Required. Inform a valid email address.', widget=forms.TextInput(attrs={'placeholder': 'Email', 'style':'margin-bottom: 10px;'}))
    about = forms.CharField(max_length=280, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Acerca de mí', 'style':'margin-bottom: 10px;'}))


class FilterForm(forms.Form):
    search=forms.CharField(
        max_length=100,
        widget= forms.TextInput(attrs={'id':'filter_search','placeholder':'Search...'}))
    user=forms.CharField(
        max_length=100,
        widget= forms.TextInput(attrs={'id':'filter_user','placeholder':'Worker...'}))
    tags=forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].widget.attrs.update({'class': 'search fluid dropdown', 'style':'display:block','id':'filter_tags'})

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tag

class UploadFileForm(forms.Form):
    file = forms.ImageField(widget=forms.FileInput(attrs={'class': 'ui primary button', 'style':'display: none', 'onchange':'loadImage(event)'}))

class UploadMCForm(forms.Form):
    mc = forms.FileField(widget=forms.FileInput(attrs={'class': 'ui primary button', 'style':'display: none', 'onchange':'loadFile(event)'}))

class ServiceAddForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    description = forms.CharField(label='Description', max_length=500, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    price = forms.IntegerField(label='Price',max_value=100000, widget=forms.TextInput(attrs={'placeholder': 'Price'}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].widget.attrs.update({'class': 'search fluid dropdown', 'style':'display:block'})

class SWSignUpForm(UserCreationForm):
    EYES = (
        ("blue", "BLUE"),
        ("brown", "BROWN"),
        )
    HAIR = (
        ("brown","BROWN"),
        ("blonde","BLONDE"),
        )
    FEMALE = 'Female'
    MALE = 'Male'
    FTM = 'Ftm'
    MTF = 'Mtf'
    GENDER_CHOICES = [
        (FEMALE , 'Female'),
        (MALE , 'Male'),
        (FTM, 'FTM'),
        (MTF, 'MTF')
    ]

    email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'validate','placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Type your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Type again your password'}))
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    third_email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.', widget=forms.TextInput(attrs={'placeholder': 'Third email'}))
    birth_date=forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'Birth date'}))
    description=forms.CharField(max_length=500, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    weight =forms.DecimalField(label='weight', widget=forms.TextInput(attrs={'placeholder': 'Weight'}))
    height =forms.DecimalField(label='height', widget=forms.TextInput(attrs={'placeholder': 'Height'}))
    # eyes = forms.MultipleChoiceField(widget=forms.RadioSelect, choices=EYES, required=False)
    # hair = forms.MultipleChoiceField(widget=forms.RadioSelect, choices=HAIR, required=False)
    # gender = forms.MultipleChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES, required=False)
    class Meta:
        model = User
        fields = (
        'username',
        'password1',
        'password2',
        'first_name',
        'last_name',
        'email',
        'description'
        )

class SWEditForm(forms.Form):
    weight =forms.DecimalField(label='weight', widget=forms.TextInput(attrs={'placeholder': 'Weight'}))
    height =forms.DecimalField(label='height', widget=forms.TextInput(attrs={'placeholder': 'Height'}))

class ServiceFilterForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

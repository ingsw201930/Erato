from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tag
from .models import SW, Appearance

class UploadFileForm(forms.Form):
    file = forms.ImageField(widget=forms.FileInput(attrs={'class': 'ui primary button', 'style':'display: none', 'onchange':'loadImage(event)'}))

class UploadAdditionalImagesForm(forms.Form):
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
    GENDER_CHOICES = SW.GENDER_CHOICES

    email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'validate','placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Type your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Type again your password'}))
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    third_email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.', widget=forms.TextInput(attrs={'placeholder': 'Third email'}))
    birth_date = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'Birth date'}))
    description = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES)

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gender'].widget.attrs.update({'class': 'ui fluid dropdown', 'style':'display:block'})

class SWAppearanceForm(forms.Form):
    EYES_CHOICES = Appearance.EYES_CHOICES
    HAIR_COLOR_CHOICES = Appearance.HAIR_COLOR_CHOICES
    HAIR_STYLES_CHOICES = Appearance.HAIR_STYLES_CHOICES
    SKIN_CHOICES = Appearance.SKIN_CHOICES

    weight = forms.DecimalField(label='weight', widget=forms.TextInput(attrs={'placeholder': 'Weight'}))
    height = forms.DecimalField(label='height', widget=forms.TextInput(attrs={'placeholder': 'Height'}))
    skin = forms.ChoiceField(choices=SKIN_CHOICES)
    eyes = forms.ChoiceField(choices=EYES_CHOICES)
    hair_style = forms.ChoiceField(choices=HAIR_STYLES_CHOICES)
    hair_color = forms.ChoiceField(choices=HAIR_COLOR_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['skin'].widget.attrs.update({'class': 'ui fluid dropdown', 'style':'display:block'})
        self.fields['eyes'].widget.attrs.update({'class': 'ui fluid dropdown', 'style':'display:block'})
        self.fields['hair_style'].widget.attrs.update({'class': 'ui fluid dropdown', 'style':'display:block'})
        self.fields['hair_color'].widget.attrs.update({'class': 'ui fluid dropdown', 'style':'display:block'})


class SWEditForm(forms.Form):
    GENDER_CHOICES = SW.GENDER_CHOICES
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    about = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    third_email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.', widget=forms.TextInput(attrs={'placeholder': 'Third email'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gender'].widget.attrs.update({'class': 'ui fluid dropdown', 'style':'display:block'})


class ServiceFilterForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')



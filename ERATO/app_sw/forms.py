from django import forms

class ServiceAddForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    description = forms.CharField(label='Description', max_length=500, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    price = forms.IntegerField(label='Price',max_value=10000000, widget=forms.TextInput(attrs={'placeholder': 'Price'}))

<<<<<<< HEAD

class SWSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.')
    birthDate=forms.DateTimeField()
    description=forms.CharField(max_length=500)
    third_email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2'
        ,'description' )
=======
class SignUp(forms.Form):
    picture_path=forms.CharField(max_length=200)
    MC_path=forms.CharField(max_length=200)
    name = forms.CharField(label='Name', max_length=100)
    birthDate=forms.DateTimeField()
    about = forms.CharField(label='About me', max_length=200)
    weigth=forms.CharField(max_length=10)
    heigth=forms.CharField(max_length=10)
    third_email=forms.CharField(max_length=200)
>>>>>>> 09fc254aa83f286652a49415ab2f4430d860d35a

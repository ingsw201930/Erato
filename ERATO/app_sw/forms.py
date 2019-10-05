from django import forms

class ServiceAddForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    description = forms.CharField(label='Description', max_length=500)
    price = forms.IntegerField(label='Price',max_value=10000000)

class SignUp(forms.Form):
    picture_path=forms.CharField(max_length=200)
    MC_path=forms.CharField(max_length=200)
    name = forms.CharField(label='Name', max_length=100)
    birthDate=forms.DateTimeField()
    about = forms.CharField(label='About me', max_length=200)
    weigth=forms.CharField(max_length=10)
    heigth=forms.CharField(max_length=10)
    third_email=forms.CharField(max_length=200)

from django import forms

class ServiceAddForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    description = forms.CharField(label='Description', max_length=500)
    price = forms.IntegerField(label='Price',max_value=10000000)

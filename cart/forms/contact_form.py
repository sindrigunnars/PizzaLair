from cart.models import ContactInformation
from django.forms import ModelForm, widgets
from django import forms


class ContactCreateForm(ModelForm):
    class Meta:
        model = ContactInformation
        exclude = ['id', 'user']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
        }

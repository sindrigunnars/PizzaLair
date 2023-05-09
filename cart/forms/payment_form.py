from django.forms import ModelForm, widgets, DateField
from datetime import datetime
from django import forms
from django.db import models


from cart.models import PaymentInformation


class PaymentCreateForm(ModelForm):

    def clean_expiry(self):
        now = datetime.now()
        date = self.cleaned_data.get('expiry')
        #month, year = date.split('/')
        month = date.month
        year = date.year
        if (now.month < month < 13) and (year >= now.year):
            return date
        elif (0 < month < now.month) and (year > now.year):
            return date
        else:
            raise forms.ValidationError('Your card is expired {}'.format(date))

    class Meta:
        model = PaymentInformation
        exclude = ['id', 'user']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'cvc': widgets.NumberInput(attrs={'class': 'form-control'}),
            'expiry': widgets.DateInput(attrs={'class': 'form-control'}, format='%m/%y'),
            'country': widgets.Select(attrs={'class': 'form-control'}),
        }

from django.forms import ModelForm, widgets, DateField
from datetime import datetime
from django import forms

from cart.models import PaymentInformation


class PaymentCreateForm(ModelForm):

    class Meta:
        model = PaymentInformation
        exclude = ['id', 'user']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'cvc': widgets.NumberInput(attrs={'class': 'form-control'}),
            'expiry': widgets.DateInput(attrs={'class': 'form-control'}, format='%m/%y'),
        }
'''
    def clean(self):
        super(PaymentCreateForm, self).clean()

        card_number = self.cleaned_data.get('card_number')
        cvc = self.cleaned_data.get('cvc')

        if len(card_number) != 16 and type(card_number) != int:
            raise forms.ValidationError('Card number must be a 16 digit number')

        if len(cvc) != 3 and type(cvc) != int:
            raise forms.ValidationError('CVC must be a 3 digit number')

    def clean_expiry(self):
        now = datetime.now()
        date = self.cleaned_data.get('expiry')
        month = date.month
        year = date.year
        if (now.month < month < 13) and (year >= now.year):
            return date
        elif (0 < month < now.month) and (year > now.year):
            return date
        else:
            raise forms.ValidationError('Your card is expired {}'.format(date))

'''
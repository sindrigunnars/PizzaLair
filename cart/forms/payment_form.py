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
            'card_number': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'xxxxxxxxxxxxxxxx'}),
            'cvc': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'xxx'}),
            'expiry': widgets.DateInput(attrs={'class': 'form-control'}),
        }

    def clean_card_number(self):
        cc_number = self.cleaned_data.get('card_number')
        if len(str(cc_number)) != 16:
            raise forms.ValidationError('Card number must be a 16 digit number written consecutively\n'
                                        '(for testing purposes use zeros)')
        return cc_number

'''
    def clean(self):
        super(PaymentCreateForm, self).clean()

        card_number = self.cleaned_data.get('card_number')
        cvc = self.cleaned_data.get('cvc')

        if len(str(card_number)) != 16:
            raise forms.ValidationError('Card number must be a 16 digit number')

        if len(str(cvc)) != 3:
            raise forms.ValidationError('CVC must be a 3 digit number')

    def clean_expiry(self):
        date = self.cleaned_data.get('expiry')
        
        if date < datetime.now():
            raise forms.ValidationError('Your card is expired {}'.format(date))
        
        return date
'''
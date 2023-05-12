from django.forms import ModelForm, widgets
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
            raise forms.ValidationError('Card number must be a 16 digit number written consecutively')
        return cc_number

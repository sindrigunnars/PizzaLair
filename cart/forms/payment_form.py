from django.forms import ModelForm, widgets

from cart.models import PaymentInformation


class PaymentCreateForm(ModelForm):
    class Meta:
        model = PaymentInformation
        exclude = ['id', 'user']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'cvc': widgets.NumberInput(attrs={'class': 'form-control'}),
            'expiry': widgets.DateInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
        }
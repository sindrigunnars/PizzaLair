from django.forms import ModelForm, widgets
from userprofile.models import UserProfile


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['id', 'user']
        widgets = {
            'screen_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'image': widgets.TextInput(attrs={'class': 'form-control'})
        }

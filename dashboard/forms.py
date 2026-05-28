from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from . import data

class CustomRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control bg-dark text-light border-secondary'
            })


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['favorite_team', 'favorite_driver']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Dynamically generate choice lists from data.py configuration
        team_choices = [('', '— Select Favorite Team —')] + [
            (t['name'], t['name']) for t in data.CONSTRUCTORS_2026
        ]
        driver_choices = [('', '— Select Favorite Driver —')] + [
            (d['code'], f"{d['name']} ({d['code']})") for d in data.DRIVERS_2026
        ]

        # Override default fields with styled choice fields
        self.fields['favorite_team'] = forms.ChoiceField(choices=team_choices, required=False)
        self.fields['favorite_driver'] = forms.ChoiceField(choices=driver_choices, required=False)

        # Style dropdown elements with Bootstrap classes
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-select bg-dark text-light border-secondary'
            })
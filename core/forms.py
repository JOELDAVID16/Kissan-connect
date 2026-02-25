from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    location = forms.CharField(max_length=100, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    role = forms.ChoiceField(choices=[('buyer', 'Buyer'), ('farmer', 'Farmer')], widget=forms.Select)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

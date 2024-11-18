# forms.py

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import re

alpha = RegexValidator(r'^[a-zA-Z_ ]*$', 'Please enter valid name.')

class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

    first_name = forms.CharField(error_messages={'required': 'Please enter first name'},validators=[alpha])
    last_name = forms.CharField(error_messages={'required': 'Please enter last name'},validators=[alpha])    
    username = forms.CharField(error_messages={'required': 'Please enter username'})
    password = forms.CharField(error_messages={'required': 'Please enter password'})
    confirm_password = forms.CharField(error_messages={'required': 'Please enter confirm password'})

    # Custom validation to check if passwords match
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")        
        return confirm_password
    
    # Optional: Additional validation for unique username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")
        return username

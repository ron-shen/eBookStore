from django import forms
from django.forms.widgets import PasswordInput
from django.forms import ModelForm, Textarea
from .models import User
from django.contrib.auth.forms import AuthenticationForm


class SignUpForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ["username", "password", "email", "first_name", "last_name", "billing_address"]
    labels = {
      "username": "User name",
      "password": "Password",
      "email": "Email",
      "first_name": "First name",
      "last_name": "Last name",
      "billing_address": "Billing address"
    }
    widgets = {
        "password": PasswordInput
    }
    
class SignInForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ["username", "password"]
    labels = {
      "username": "User name",
      "password": "Password",
    }
    widgets = {
        "password": PasswordInput
    }
    
class SignInForm(AuthenticationForm):
    """
    Sign in form 
    """
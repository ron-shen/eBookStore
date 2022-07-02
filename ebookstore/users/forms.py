from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'password', 'email', 'first_name', 'last_name', 'billing_address']
    labels = {
      "username": "User name",
      "password": "Password",
      "email": "Email",
      "first_name": "First name",
      "last_name": "Last name",
      "billing_address": "Billing address"
    } 
    
class SignInForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'password']
    labels = {
      "username": "User name",
      "password": "Password",
    } 
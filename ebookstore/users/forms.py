from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['user_name', 'password', 'email', 'first_name', 'last_name', 'billing_address']
    labels = {
      "user_name": "User name",
      "password": "Password",
      "email": "Email",
      "first_name": "First name",
      "last_name": "Last name",
      "billing_address": "Billing address"
    } 
    
class SignInForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['user_name', 'password']
    labels = {
      "user_name": "User name",
      "password": "Password",
    } 
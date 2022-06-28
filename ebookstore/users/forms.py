from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
  class Meta:
    model = User
    labels = {
      "user_name": "User name",
      "password": "Password",
      "email": "Email",
      "first_name": "First name",
      "last_name": "Last name",
      "billing_address": "Billing address"
    } 
    
class SignUpForm(forms.ModelForm):
  class Meta:
    model = User
    exclude = ["email", "first_name", "last_name", "billing_address"]
    labels = {
      "user_name": "User name",
      "password": "Password",
      "email": "Email",
      "first_name": "First name",
      "last_name": "Last name",
      "billing_address": "Billing address"
    } 
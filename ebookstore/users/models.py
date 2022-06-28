from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    billing_address = models.CharField(max_length=100)

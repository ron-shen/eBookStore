from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from ebooks.models import Book

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    billing_address = models.CharField(max_length=100)
    
    
class WishList(models.Model):
	#since Django doesn't support composite primary keys,
	#unique_together need to be used ot act as composite primary keys
	class Meta:
		unique_together = ['user', 'book']

	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	date = models.DateField(auto_now_add=True)

	def __str__(self):
		return f"{self.user_id}, {self.book_id}"

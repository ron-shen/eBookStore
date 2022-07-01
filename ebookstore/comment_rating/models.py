from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class CommentRating(models.Model):
	comment = models.TextField(max_length=500)
	rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
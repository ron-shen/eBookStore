from django import forms
#from .models import CommentRating


class CommentRatingForm(forms.Form):
	comment = forms.TextField(max_length=500)
	rating = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
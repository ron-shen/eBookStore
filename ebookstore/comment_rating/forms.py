from django import forms
from .models import CommentRating


class CommentRatingForm(forms.ModelForm):
  class Meta:
    model = CommentRating
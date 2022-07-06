from django.forms import ModelForm
from .models import UserBook


class CommentRatingForm(ModelForm):
    class Meta:
        model = UserBook
        fields = ['comment', 'rating']
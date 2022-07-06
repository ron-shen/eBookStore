import string
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from django.views.generic.list import ListView
from .models import Book, UserBook
from .forms import CommentRatingForm
from users.models import User



# Create your views here.
class Homepage(ListView):
    template_name = "ebooks/index.html"
    model = Book
    context_object_name = "books"
    ordering = ["-copies_sold"]
        
    def get_queryset(self):
        books = super().get_queryset()
        books = books[:5]
        return books
  
  
class EbookDetailView(View):
    def get(self, request, slug):
        book = Book.objects.get(slug=slug)
        users_comment_rating = []
        rating_distribution = [0] * 5 #distribution of rating 1 2 3 4 5
        avg_rating = 0
        for comment_rating in UserBook.objects.filter(book=book.id, 
                                                      comment__isnull=False,
                                                      rating__isnull=False):
            username = User.objects.get(pk=comment_rating.user.id)
            users_comment_rating.append((username, comment_rating.comment, comment_rating.rating))
            rating_distribution[comment_rating.rating - 1] += 1
        
        for i in range(len(rating_distribution)):
            avg_rating += (i + 1) * rating_distribution[i]
        try:
            avg_rating /= sum(rating_distribution)
        except ZeroDivisionError:
            pass
        
        #only generate the comment rating form when the user 
        #1. bought the book and 
        #2. haven't given the comment and rating yet
        user_bought_book = UserBook.objects.filter(user=request.user.id, book=book.id)
        user_bought_book = user_bought_book.filter(comment__isnull=True, rating__isnull=True).exists()
        comment_rating_form = None
        if user_bought_book:
            comment_rating_form = CommentRatingForm()
            
        content = {"book": book, "users_comment_rating": users_comment_rating, "rating_distribution": rating_distribution, 
                   "avg_rating": avg_rating, "comment_rating_form": comment_rating_form}
        
        return render(request, "ebooks/details.html", content)


    def post(self, request):
        pass
  

class EbooksView(ListView):
	template_name = "ebooks/ebooks.html"
	model = Book
	context_object_name = "books"




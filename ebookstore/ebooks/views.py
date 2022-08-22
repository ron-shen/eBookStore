import string
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from .models import Book, UserBook
from .forms import CommentRatingForm
from users.models import User
from django.urls import reverse



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
  
  
class EbookDetailView(FormView):
    template_name = "ebooks/details.html"
    form_class = CommentRatingForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
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
        user_bought_book = UserBook.objects.filter(user=self.request.user.id, book=book.id)
        user_bought_book = user_bought_book.filter(comment__isnull=True, rating__isnull=True).exists()
        show_form = False
        if user_bought_book:
            show_form = True
            
        context["book"] = book 
        context["users_comment_rating"] = users_comment_rating
        context["rating_distribution"] = rating_distribution
        context["avg_rating"] = avg_rating
        context["show_form"] = show_form
        
        return context
    

    def post(self, request, slug):
        if "comment_rating" in request.POST:
            form = CommentRatingForm(request.POST)
            if form.is_valid():           
                book_id = int(request.POST["book_id"])
                user_id = request.user.id
                comment = request.POST["comment"]
                rating = request.POST["rating"]
                UserBook.objects.filter(user=user_id, book=book_id).update(comment=comment, 
                                                                        rating=rating)
                return HttpResponseRedirect(reverse("indiviudal-ebook", args=[slug]))

            else:
                print(form.errors.as_data())
                return self.form_invalid(form)                     
  

class EbooksView(ListView):
	template_name = "ebooks/ebooks.html"
	model = Book
	context_object_name = "books"




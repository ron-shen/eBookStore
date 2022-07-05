from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from django.views.generic.list import ListView
from .models import Book, UserBook
 


# Create your views here.
class Homepage(ListView):
	template_name = "ebooks/index.html"
	model = Book
	context_object_name = "books"
  
  
class EbookDetailView(View):
    def get(self, request, slug):
        book = Book.objects.get(slug=slug)
        comment = []
        rating = [0] * 5 #distribution of rating 1 2 3 4 5
        avg_rating = 0
        for comment_rating in UserBook.objects.filter(book__id=book.id):
            comment.append(comment_rating.comment)
            rating[comment_rating.rating] += 1
        
        for i in range(len(rating)):
            avg_rating += (i + 1) * rating[i]
        try:
            avg_rating /= sum(rating)
        except ZeroDivisionError:
            pass
            
        content = {"book": book, "comment": comment, "rating": rating, 
                   "avg_rating": avg_rating}
        return render(request, "ebooks/details.html", content)

    def post(self, request):
        pass
  

class EbooksView(ListView):
	template_name = "ebooks/ebooks.html"
	model = Book
	context_object_name = "books"




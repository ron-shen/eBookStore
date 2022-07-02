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
        comment_rating = UserBook.objects.filter(book__id=book.id)
        content = {"book": book, "comment_rating": comment_rating}
        return render(request, "ebooks/details.html", content)

    def post(self, request):
        pass
  

class EbooksView(ListView):
	template_name = "ebooks/ebooks.html"
	model = Book
	context_object_name = "books"




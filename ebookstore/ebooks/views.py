from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from django.views.generic.list import ListView
from .models import Book


# Create your views here.
class Homepage(ListView):
  template_name = "ebooks/index.html"
  model = Book
  


class EbookDetailView(View):
  def get(self, request, slug):
    return HttpResponse("ebook")
  
  def post(self, request):
    pass
  

class EbooksView(ListView):
  def get(self, request):
    return HttpResponse("overall books")




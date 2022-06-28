from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.list import ListView


# Create your views here.
class Homepage(ListView):
  pass


class EbookDetailView(View):
  def get(self, request):
    pass
  
  def post(self, request):
    pass
  

class EbooksView(ListView):
  pass




from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic.base import View

# Create your views here.
class CartView(LoginRequiredMixin, ListView):
    redirect_field_name = "indiviudal-ebook"

    def add_book_to_cart(self, request):
        #add book id into session
        added_book = request.session.get("cart")
        if added_book is None:
            added_book = []
        
        book_id = int(request.POST["book_id"])
        if book_id not in added_book:
            added_book.append(book_id)
            request.session["cart"] = added_book
        
    
    def get(self, request):
        return render(request, "cart/cart.html")

  
    def post(self, request):
        if 'add_to_cart' in request.POST:
            self.add_book_to_cart(request)      
            return HttpResponseRedirect(reverse("indiviudal-ebook", args=[request.POST["slug"]]))
        
        if 'buy_now' in request.POST:
            self.add_book_to_cart(request)
            return HttpResponseRedirect(reverse("cart"))
            
        # return HttpResponse("cart")
        

class CheckOutView(View):
    def get(self, request):
        pass
    
    def post(self, request):
        return HttpResponse("Success")
        
    
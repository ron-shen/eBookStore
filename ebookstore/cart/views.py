from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
#from django.views.generic.base import View
from ebooks.models import Book, UserBook
from users.models import User

# Create your views here.
class CartView(LoginRequiredMixin, ListView):
    redirect_field_name = "indiviudal-ebook"
    model = Book
    context_object_name = "books"
    template_name = "cart/cart.html"
  
    def add_book_to_cart(self, request):
        #add book id into session
        added_book = request.session.get("cart")
        if added_book is None:
            added_book = []
        
        book_id = int(request.POST["book_id"])
        if book_id not in added_book:
            added_book.append(book_id)
            request.session["cart"] = added_book
           
    # def get(self, request):
    #     self.get_queryset()
    #     return render(request, "cart/cart.html")  
    def get_queryset(self):
        books_in_cart = self.request.session.get("cart", [])
        books = super().get_queryset()
        books = books.filter(pk__in=books_in_cart)
        return books
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_price = 0
        query_set = context["books"]
        for book in query_set:
            total_price += book.price      
        context["total_price"] = total_price
        
        return context
        
 
    def post(self, request):
        if "add_to_cart" in request.POST:
            self.add_book_to_cart(request)    
            return HttpResponseRedirect(reverse("indiviudal-ebook", args=[request.POST["slug"]]))
        
        if "buy_now" in request.POST:
            self.add_book_to_cart(request)
            return HttpResponseRedirect(reverse("cart"))
        
        if "delete" in request.POST:
            book_id = int(request.POST["delete"])
            books_in_cart = request.session.get("cart")
            books_in_cart.remove(book_id)
            request.session["cart"] = books_in_cart
            return HttpResponseRedirect(reverse("cart"))
        
        if "checkout" in request.POST:
            books_in_cart = request.session.get("cart")
            user = User.objects.get(pk=request.user.id)
            books = Book.objects.filter(pk__in=books_in_cart)
            for book in books:
                #Duplicate entry            
                UserBook.objects.create(user=user, book=book)                          
            del request.session["cart"]            
            return HttpResponseRedirect(reverse("home-page"))

# class CheckOutView(View):
#     def get(self, request):
#         pass
    
#     def post(self, request):
#         return HttpResponse("Success")
        
    
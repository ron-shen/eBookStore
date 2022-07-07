from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from .forms import SignUpForm, SignInForm
from django.contrib.auth import authenticate, login
from .models import User, WishList
from ebooks.models import Book
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.db import IntegrityError
from django.views.generic.base import View
from ebooks.models import UserBook
from django.conf import settings
from django.contrib.auth.hashers import make_password


# Create your views here.
def account_view(request):
    # user = authenticate(username='test', password='password')
    # if user is not None:
    #     print(user.get_username())
    #     return HttpResponse("OK!")
    # else:
    #     return HttpResponse("no")
    #show link to user profile, purchase history and books owned
    return render(request, "users/user.html")


class ProfileView(LoginRequiredMixin, FormView):
    redirect_field_name = "home-page"
    template_name = "users/profile.html"
    form_class = SignUpForm
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(pk=self.request.user.id)
        user.password = None
        form = SignUpForm(instance=user)
        context["form"] = form
        return context

   
    def post(self, request):
        form = SignUpForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(user.password)
            user.save()
            return HttpResponseRedirect(reverse("home-page"))   
        else:
            print(form.errors.as_data())
            return self.form_invalid(form)

       
    def form_invalid(self, form):
        #the default form_invalid() calls get_context_data() I overwrite,
        #which overwrite the inputted data, so I have to overide this method
        #to call the parent get_context_data
        return self.render_to_response(super().get_context_data(form=form))
    

class PurchaseHistory(LoginRequiredMixin, ListView):
    redirect_field_name = "home-page"
    model = UserBook
    context_object_name = "user_books"
    template_name = "users/purchase_history.html"
        
    def get_queryset(self):
        user_id = self.request.user.id
        user_books = super().get_queryset()
        user_books = user_books.filter(user=user_id)
        return user_books

 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        history = []
        print("test", context["user_books"])
        for user_book in context["user_books"]:
            book = Book.objects.get(pk=user_book.book.id)
            history.append((book.title, book.price, user_book.date))
        
        context["history"] = history
        return context
    

class LibraryView(LoginRequiredMixin, View):
    #show all the books users bought
    redirect_field_name = "home-page"
    
    def get(self, request):
        user_id = request.user.id
        book_bought = UserBook.objects.values_list("book", flat=True).filter(user=user_id)
        books = Book.objects.filter(pk__in=book_bought)
        context = {"books": books}
        return render(request, "users/library.html", context=context)
    
    def post(self, request):
        file = "books_pdf/" + request.POST["slug"] + ".pdf"
        path = settings.MEDIA_ROOT / file
        response = FileResponse(open(path, 'rb'))
        return response
        
     
class SignInView(FormView):
    template_name = "users/sign_in.html/"
    form_class = SignInForm
    
  
    def post(self, request):
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse("home-page"))
        
        else:
            print(form.errors.as_data())
            return self.form_invalid(form)
         
        # user = authenticate(username=request.POST['username'], 
        #                     password=request.POST['password'])
        # print(type(user))
        # print(dir(user))
        # if user is not None:
        #     #print("user exist")
        #     login(request, user)
        # else:
        #     return HttpResponse("user doesn't exist!")
        
        # # if request.user.is_authenticated:
        # #     print(user.username)
        # #     print("ok!!!!!!!!!!!!!!!!!!!")
            
        # # else:
        # #     print("not ok!!!")
            
        #return HttpResponseRedirect(reverse("home-page"))


class SignUpView(FormView):
    template_name = "users/sign_up.html/"
    form_class = SignUpForm
    
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(user.password)
            user.save()
            return HttpResponseRedirect(reverse("home-page"))
        else:
            #keep the inputted data in the sign up page
            #and input the invalid field
            print(form.errors.as_data())
            return self.form_invalid(form)

            
class WishListView(LoginRequiredMixin, View):
    redirect_field_name = "home-page"
    
    def get(self, request):  
        user_id = self.request.user.id
        wishlist = WishList.objects.values_list("book", flat=True).filter(user=user_id)
        books = Book.objects.filter(pk__in=wishlist)
        return render(request, "users/wishlist.html", {"books":books})
          
    
    def post(self, request):
        if "add_to_wishlist" in request.POST:
            book = Book.objects.get(slug=request.POST["slug"])
            #if the book already exists in the wishlist, raise IntegrityError
            try:
                WishList.objects.create(user=request.user, book=book)
            except IntegrityError:
                pass
            
            return HttpResponseRedirect(reverse("indiviudal-ebook", args=[request.POST["slug"]]))

        if "delete" in request.POST:
            book_id = int(request.POST["delete"])
            user_id = request.user.id
            WishList.objects.filter(book=book_id, user=user_id).delete()
            return HttpResponseRedirect(reverse("wish-list"))
    

def signout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home-page"))

  
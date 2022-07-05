from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignUpForm, SignInForm
from django.contrib.auth import authenticate, login
from .models import User, WishList
from ebooks.models import Book
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout



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


class ProfileView(LoginRequiredMixin, UpdateView):
    redirect_field_name = "home-page"
    
    def get(self, request):
        return HttpResponse("profile")
    

class PurchaseHistory(LoginRequiredMixin, ListView):
    redirect_field_name = "home-page"
    
    def get(self, request):
        return HttpResponse("purchasehistory")
    

class LibraryView(LoginRequiredMixin, ListView):
    redirect_field_name = "home-page"
    
    #show all the books users bought
    def get(self, request):
        return HttpResponse("library")


class SignInView(FormView):
    template_name = "users/sign_in.html/"
    form_class = SignInForm
    
    def post(self, request):
        user = authenticate(username=request.POST['username'], 
                            password=request.POST['password'])
        if user is not None:
            login(request, user)
        # else:
        #     return HttpResponse("user doesn't exist!")
        
        # if request.user.is_authenticated:
        #     print(user.username)
        #     print("ok!!!!!!!!!!!!!!!!!!!")
            
        # else:
        #     print("not ok!!!")
            
        return HttpResponseRedirect(reverse("home-page"))


class SignUpView(FormView):
    template_name = "users/sign_up.html/"
    form_class = SignUpForm
    
    def post(self, request):
        form = self.get_form()
        if form.is_valid():        
            return self.form_valid(form)
        else:
            print(form.errors.as_data())
        return HttpResponse("bad") 
    
    def form_valid(self, form):
        user = form.save(commit=False)
        User.objects.create_user(username=user.username, email=user.email, password=user.password,
                            first_name=user.first_name, last_name=user.last_name, 
                            billing_address=user.billing_address)
        return HttpResponseRedirect(reverse("home-page"))
    

class WishListView(LoginRequiredMixin, ListView):
    redirect_field_name = "home-page"
    
    def get(self, request):
        print(request.user.username)
        return HttpResponse("wish list")

    def post(self, request):
        book = Book.objects.get(slug=request.POST["slug"])
        WishList.objects.create(user=request.user, book=book)
        return HttpResponseRedirect(reverse("indiviudal-ebook", args=[request.POST["slug"]]))
    

def signout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home-page"))

  
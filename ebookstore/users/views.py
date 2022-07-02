from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.http import HttpResponse
from .forms import SignUpForm, SignInForm
from django.contrib.auth import authenticate


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


class ProfileView(UpdateView):
    def get(self, request):
        return HttpResponse("profile")


class PurchaseHistory(ListView):
    def get(self, request):
        return HttpResponse("purchasehistory")


class LibraryView(ListView):
    #show all the books users bought
    def get(self, request):
        return HttpResponse("library")


class SignInView(FormView):
    template_name = "users/sign_in.html/"
    form_class = SignInForm


class SignUpView(FormView):
    template_name = "users/sign_up.html/"
    form_class = SignUpForm


class WishListView(ListView):
    def get(self, request):
        return HttpResponse("wish list")


  
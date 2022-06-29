from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.http import HttpResponse


# Create your views here.
def account_view(request):
  #show link to user profile, purchase history and books owned
  return HttpResponse("account overview")


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
  def get(self, request):
    return HttpResponse("sign in")


class SignUpView(FormView):
  def get(self, request):
    return HttpResponse("sig up")


class WishListView(ListView):
  def get(self, request):
    return HttpResponse("wish list")


  
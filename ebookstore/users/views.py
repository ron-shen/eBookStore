from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView


# Create your views here.
def user_view(request):
  #show link to user profile, purchase history and books owned
  pass


class ProfileView(UpdateView):
  pass


class PurchaseHistory(ListView):
  pass


class LibraryView(ListView):
  #show all the books users bought
  pass


class SignInView(FormView):
  pass


class SignUpView(FormView):
  pass


class WishListView(ListView):
  pass 


  
from django.urls import path
from . import views


urlpatterns = [
  path("", views.account_view, name="account"),
  path("profile/", views.ProfileView.as_view(), name="profile"),   
  path("purchasehistory/", views.PurchaseHistory.as_view(), name="purchase-history"),
  path("library/", views.LibraryView.as_view(), name="library"),
  path("wishlist/", views.WishListView.as_view(), name="wish-list"),
  path("signin/", views.SignInView.as_view(), name="sign-in"),
  path("signup/", views.SignUpView.as_view(), name="sign-up"),
  path("signout/", views.signout_view, name="sign-out"),
]
from django.urls import path
from . import views


urlpatterns = [
  path("", views.Homepage.as_view(), name="home-page"),
  path("ebooks/", views.EbooksView.as_view(), name="ebooks"),   
  path("ebooks/<slug:slug>/", views.EbookDetailView.as_view(), name="indiviudal-ebook"),
]

from django.contrib import admin
from .models import Author, Category, Publisher, Book, UserBook
# Register your models here.

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(UserBook)
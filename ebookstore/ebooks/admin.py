from django.contrib import admin
from .models import Author, Category, Publisher, Book, UserBook
# Register your models here.
class BookAdmin(admin.ModelAdmin):
  list_display = ("title", "publisher", "date",)
  prepopulated_fields = {"slug": ("title",)}


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(Book, BookAdmin)
admin.site.register(UserBook)
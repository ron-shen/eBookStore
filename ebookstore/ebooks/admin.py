from django.contrib import admin
from .models import Author, Category, Publisher, Book, UserBook
from django.contrib.sessions.models import Session

# Register your models here.
class BookAdmin(admin.ModelAdmin):
	list_display = ("title", "publisher", "date",)
	prepopulated_fields = {"slug": ("title",)}

class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(Book, BookAdmin)
admin.site.register(UserBook)
    
admin.site.register(Session, SessionAdmin)



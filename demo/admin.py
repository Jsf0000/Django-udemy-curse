from django.contrib import admin
from .models import Book

# admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields = ['title']
    list_display = ['title', 'price']
    list_filter = ['published']
    search_fields = ['title']
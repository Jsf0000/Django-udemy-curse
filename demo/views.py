from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book


#
# class Another(View):
#
#     books = Book.objects.filters(is_published=True)
#
#     output = '\n'
#
#     for book in books:
#         output += f"We have {book.title} book with ID {book.id} in DB<br>"
#
#     def get(self, request):
#         return HttpResponse(self.output)


def first(request):

    books = Book.objects.all()

    return render(request, 'first_temp.html', {'books': books})

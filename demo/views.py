from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer, BookMineSerializer


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

class BookViewSet(viewsets.ModelViewSet):
    # Default serializer
    serializer_class = BookMineSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # for get method
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)


from rest_framework import serializers
from .models import Book, BookNumber, Characters, Author

class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ['id','isbn_10', 'isbn_13']

class BookCharactersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characters
        fields = ['id','name']

class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name', 'surname']

class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False)
    characters = BookCharactersSerializer(many=True)
    authors = BookAuthorSerializer(many=True)
    class Meta:
        model = Book
        fields = ['id','title', 'description', 'price', 'is_published', 'published', 'number',
                  'characters', 'authors']

class BookMineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','price']
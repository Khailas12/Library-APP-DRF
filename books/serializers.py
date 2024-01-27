from rest_framework import serializers

from author.models import Author
from .models import Books


class BooksSerializer(serializers.ModelSerializer):
    author_email = serializers.EmailField(source='author.email', read_only=True)
    book_id = serializers.CharField(source='books.book_id',read_only=True)
    # author_name = serializers.CharField(source='author.name', read_only=True)
    
    class Meta:
        model = Books
        fields = '__all__'
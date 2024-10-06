from rest_framework import serializers
from .models import Author, Category, Book

class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='book-detail'
    )

    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_date', 'books']


class CategorySerializer(serializers.ModelSerializer):
    books = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='book-detail'
    )

    class Meta:
        model = Category
        fields = ['id', 'name', 'books']


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='name')
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'publication_date', 'category', 'author']

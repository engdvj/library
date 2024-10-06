from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Author, Book, Category
from .serializers import AuthorSerializer, BookSerializer, CategorySerializer
from django.urls import NoReverseMatch

# View para listar e criar livros
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-list'

# View para detalhar, atualizar e deletar livros
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-detail'

# View para listar e criar autores
class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    name = 'author-list'

# View para detalhar, atualizar e deletar autores
class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    name = 'author-detail'

# View para listar e criar categorias
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-list'

# View para detalhar, atualizar e deletar categorias
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-detail'

class ApiRoot(APIView):
    def get(self, request, *args, **kwargs):
        # Gera os links e explicações dos endpoints
        context = {
            'Authors': {
                'List': {
                    'description': 'Para listar todos os autores',
                    'link': reverse('author-list', request=request)
                },
                'Detail': {
                    'description': 'Para detalhar, atualizar ou deletar um autor (exemplo com id=1)',
                    'link': reverse('author-detail', kwargs={'pk': 1}, request=request)
                },
            },
            'Books': {
                'List': {
                    'description': 'Para listar todos os livros',
                    'link': reverse('book-list', request=request)
                },
                'Detail': {
                    'description': 'Para detalhar, atualizar ou deletar um livro (exemplo com id=1)',
                    'link': reverse('book-detail', kwargs={'pk': 1}, request=request)
                },
            },
            'Categories': {
                'List': {
                    'description': 'Para listar todas as categorias',
                    'link': reverse('category-list', request=request)
                },
                'Detail': {
                    'description': 'Para detalhar, atualizar ou deletar uma categoria (exemplo com id=1)',
                    'link': reverse('category-detail', kwargs={'pk': 1}, request=request)
                },
            }
        }
        return Response(context)
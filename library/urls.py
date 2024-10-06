from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.author_list, name='author-list'),
    path('authors/<int:pk>/', views.author_detail, name='author-detail'),
    path('categories/', views.category_list, name='category-list'),
    path('categories/<int:pk>/', views.category_detail, name='category-detail'),
    path('books/', views.book_list, name='book-list'),
    path('books/<int:pk>/', views.book_detail, name='book-detail'),
]

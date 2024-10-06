from django.urls import include, path
from library import views

urlpatterns = [
    path('api/', views.ApiRoot.as_view(), name='api-root'),
    path('api/books/', views.BookList.as_view(), name='book-list'),
    path('api/books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
    path('api/authors/', views.AuthorList.as_view(), name='author-list'),
    path('api/authors/<int:pk>/', views.AuthorDetail.as_view(), name='author-detail'),
    path('api/categories/', views.CategoryList.as_view(), name='category-list'),
    path('api/categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
]

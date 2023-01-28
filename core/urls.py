from django.urls import path, include
from . import views
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('books/', views.BookListView.as_view(), name='books_list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('status/', views.StatusView.as_view(), name='status'),
    path('books/featured', views.FeaturedBookList.as_view(), name='featured_list'),
]
from django.urls import path, include
from . import views
from django.contrib import admin
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('books/', views.BookView.as_view(), name='books_list'),
    path('books/<int:pk>/', views.BookView.as_view(), name='book_detail'),
    path('status/', views.StatusView.as_view(), name='status'),
    path('status/<int:pk>', views.StatusDetailView.as_view(), name='status_detail'),
    path('featured/', views.FeaturedView.as_view(), name='featured_list'),
    path('featured/edit/<int:pk>/', views.FeaturedView.as_view(), name='featured_edit'),
    path('notes/', views.NoteView.as_view(), name='note_list'),
    path('notes/add/', views.NoteView.as_view(), name='note_add'),
]
from .models import Book, Status
from rest_framework import generics, permissions
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
# from rest_framework.response import Response
# from rest_framework.decorators import APIView
from .serializers import BookSerializer, StatusSerializer, FeaturedSerializer


class ListBook(generics.ListCreateAPIView):
    queryset = Book.objects.values_list('title', 'author')
    serializer = BookSerializer()
    permissions = permissions.IsAuthenticatedOrReadOnly

    def get_queryset(self):
        return self.request.user.books.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class BookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer = BookSerializer()

class StatusView(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer = StatusSerializer()
    permissions = permissions.IsOwnerOrReadOnly

    def create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Status.objects.filter(user=self.request.user)
        return queryset

class FeaturedView(generics.ListAPIView):
    queryset = Book.objects.filter(feature=True)
    serializer = FeaturedSerializer
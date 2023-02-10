from .models import Book, Status, Note
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.response import Response
# from rest_framework.decorators import APIView
from .serializers import BookSerializer, StatusSerializer, FeaturedSerializer, NoteSerializer


class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permissions = permissions.IsAuthenticatedOrReadOnly

    def get_queryset(self):
        return self.request.user.books.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

# class BookView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer = BookSerializer()

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class StatusView(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permissions = permissions.IsAuthenticatedOrReadOnly

    def create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Status.objects.filter(user=self.request.user)
        return queryset

class StatusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class FeaturedView(generics.ListAPIView):
    queryset = Book.objects.filter(featured=True)
    serializer_class = FeaturedSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.books.filter(featured=True)

class NoteView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     return self.request.user.notes.all()

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
from rest_framework import serializers
from .models import User, Book, Status

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'featured', 'pub_date')

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('user', 'status', 'book')

class FeaturedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author')
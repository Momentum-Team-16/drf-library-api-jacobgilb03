from rest_framework import serializers
from .models import User, Book, Status, Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class BookSerializer(serializers.ModelSerializer):
    statuses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    notes = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['title', 'author', 'pub_date', 'featured', 'statuses', 'notes']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('user', 'state', 'book')

class FeaturedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author')

class NoteSerializer(serializers.ModelSerializer):
    book = serializers.CharField(source='book.title')
    class Meta:
        model = Note
        fields = ['book', 'entry']

    # def create(self, validated_data):
    #     return models.Notes.objects.create(**validated_data)
    #     or
    #     return super(BookSerializer, self).create(validated_data)

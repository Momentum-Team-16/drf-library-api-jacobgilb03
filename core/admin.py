from django.contrib import admin
from .models import User, Book, Status, Note

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Status)
admin.site.register(Note)
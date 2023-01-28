from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint

class User(AbstractUser):
    pass

STATUS_CHOICES = (
    ('Want to read', 'WANT TO READ'),
    ('Reading', 'READING'),
    ('Read', 'READ'),
)

class Book(models.Model):
        title = models.CharField(max_length=250)
        author = models.CharField(max_length=250)
        # genre = models.CharField(max_length=50, default='Nonfiction', choices=GENRES)
        featured = models.BooleanField(default=False)
        pub_date = models.DateField()

        class Meta:
            constraints = [
                UniqueConstraint(
                    fields = ['title', 'author'], name = 'unique_book'
                )
            ]

        def __str__(self):
            return f'{self.title} by {self.author}'


class Status(models.Model):
    state = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = 'Want to read')
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    book = models.ForeignKey(Book, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.state}'
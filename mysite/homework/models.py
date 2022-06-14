from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=120)
    year_of_public = models.DateField()
    genre = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.name


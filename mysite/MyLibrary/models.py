from django.db import models

# Create your models here.
class MyUser(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class MyAuthor(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class MyBook(models.Model):
    name = models.CharField(max_length=120)
    year_of_public = models.DateField()
    genre = models.CharField(max_length=120)
    author = models.ManyToManyField(MyAuthor)
    takenBy = models.ForeignKey(MyUser, on_delete=models.CASCADE, blank=True, null=True)
    isAvaliable = models.BooleanField()

    def __str__(self):
        return self.name


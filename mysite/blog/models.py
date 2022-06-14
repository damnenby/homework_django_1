from django.db import models

# Create your models here.

#Смог только так сделать статус (просто создал 2 объекта лайк и дизлайк)
class Status(models.Model):
    status = models.CharField(max_length=10)
    def __str__(self):
        return self.status


class BlogUser(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey(BlogUser, on_delete=models.CASCADE, default='1')
    text = models.TextField()


class MyArticle(models.Model):
    author = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.ManyToManyField(Comment, blank=True, null=True)
    def __str__(self):
        return self.title



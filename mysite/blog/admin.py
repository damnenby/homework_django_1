from django.contrib import admin

# Register your models here.
from .models import BlogUser, Status, MyArticle, Comment

admin.site.register(BlogUser)
admin.site.register(Status)
admin.site.register(MyArticle)
admin.site.register(Comment)
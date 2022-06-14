from django.contrib import admin

# Register your models here.
from .models import MyAuthor, MyBook,  MyUser

admin.site.register(MyAuthor)
admin.site.register(MyBook)
admin.site.register(MyUser)
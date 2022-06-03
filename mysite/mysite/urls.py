"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from homework.views import test, dynamic_test, dynamic_test_archieve, test_users, regex, test_number

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test),
    path('articles/', test),
    path('articles/archive', test),
    path('users', test),
    path('article/<int:article_number>', dynamic_test),
    path('article/<int:article_number>/archive', dynamic_test_archieve),
    path('users/<int:user_number>', test_users),
    re_path(r'^(?P<text>\d{3}[a-zA-Z]{2,}$)', regex),
    re_path(r'^(?P<text>(?:050|093|067|096|097|098|066|095|099|063|073|093|091|092|094)[0-9]{7}$)', test_number)
]
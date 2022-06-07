from random import randint, choices
from string import ascii_letters, digits

from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def first(request):
    return render(request, 'articles.html')

def articles(request):
    return render(request, 'articles.html')

def archieve(request):
    return render(request, 'archieve.html')

def users(request):
    return render(request, 'users.html')

def article_number(request, article_number):
    return render(request, 'article_number.html', {
        "article_number": article_number
    })


def slug_text(request, article_number, slug_text):
    return render(request, 'article_number.html', {
        "article_number": article_number,
        "slug_text": slug_text
    })


def generate_random_int():
    return randint(1,100)

def generate_random_slug():
    return ''.join(choices(ascii_letters + digits, k = randint(5,10)))

def index(request):
    return render(request, 'index.html', {
        "randint": generate_random_int(),
        "randslug": generate_random_slug()
        
    })

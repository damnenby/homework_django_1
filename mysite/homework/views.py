from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test(request):
    return HttpResponse("Hey! It's your main view!!")

def dynamic_test(request, article_number):
    return HttpResponse(f"Successfully! {article_number}.")

def dynamic_test_archieve(request, article_number):
    return HttpResponse(f"Successfully! {article_number}. Archieve.")

def test_users(request, user_number):
    return HttpResponse(f"Successfully! {user_number} is your user number")

def regex(request, text):
    return HttpResponse(f"it's regexp with text: {text}")

def test_number(request, text):
    return HttpResponse(f"number is right: {text}")
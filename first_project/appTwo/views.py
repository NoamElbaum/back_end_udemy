from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def two(request):
    return HttpResponse('<em>My Second App</em>')

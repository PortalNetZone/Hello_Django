from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello(request):
    greet1 = 'Hello, Django!!!'
    return HttpResponse(greet1)

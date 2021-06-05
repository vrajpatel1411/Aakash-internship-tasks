from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("Welcome to Django")

def sum(request):
    a=10;
    b=200;
    return HttpResponse(a+b); 
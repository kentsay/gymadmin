from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    a = 10
    b = 20
    c = a+b
    return HttpResponse("<h1>Hello world. You're in dashboard " + str(c) + "</h1>")

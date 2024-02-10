from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    dict = {
        "a": "123",
    }
    return render(request, 'index.html', dict)

def aboutUs(request):
    return HttpResponse("<h1>About Us</h1>")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, 'register.html')
from django.shortcuts import render

# Create your views here.

def loginFunction(request):
    return render(request, "login.html")

def registerFunction(request):
    return render(request, "register.html")

def notFoundFunction(request):
    return render(request, "404.html")
from django.shortcuts import render

# Create your views here.

def dashboardFunction(request):
    return render(request, 'dashboard.html')
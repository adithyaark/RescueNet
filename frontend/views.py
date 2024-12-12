from django.shortcuts import render

def index(request):
    return render(request, 'html/index.html')

def home(request):
    return render(request, 'html/home.html')

def login_view(request):
    return render(request, 'html/login.html')

def register(request):
    return render(request, 'html/register.html')

def support(request):
    return render(request, 'html/support.html')

def volunteer(request):
    return render(request, 'html/volunteer.html')

def add_disaster(request):
    return render(request, 'html/add-disaster.html')



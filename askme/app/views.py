from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base.html')

def tag(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'base.html')

def signup(request):
    return render(request, 'base.html')

def ask(request):
    return render(request, 'base.html')

def settings(request):
    return render(request, 'base.html')

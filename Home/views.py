from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,('home/index.html'))

def registration(request):
    return render(request,'home/registration.html')

def about(request):
    return render(request,'home/About.html')
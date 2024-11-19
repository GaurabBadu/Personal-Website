from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def homePage(request):
    return render(request, 'header.html')

def About(request):
    return render(request, 'about.html')

def Experience(request):
    return render(request, 'Experience.html')

def Projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')

from django.shortcuts import render
from .models import Phone

def home(request):
    return render(request,'home.html')

def noutbooks(request):
    return render(request,'noutbook.html')


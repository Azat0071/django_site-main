from django.shortcuts import render
from .models import Phone

def home(request):
    return render(request,'home.html')

def smartphones(request):
    return render(request,'smartphones.html')

def noutbooks(request):
    return render(request,'noutbook.html')

def wathchas(request):
    return render(request,'watches.html')

def musics(request):
    return render(request,'music.html')

def smartphones(request):
    phones = Phone.objects.all()
    return render(request, "smartphones.html", {"phones": phones})

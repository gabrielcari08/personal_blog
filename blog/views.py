from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles

# Create your views here.

def hello(request): #Vista de prueba
    return HttpResponse("Hello World")

def list_articles(request):
    articles = Articles.objects.all()
    return render(request, 'home.html', {"articles": articles})
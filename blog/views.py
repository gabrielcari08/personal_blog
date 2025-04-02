from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Articles

# Create your views here.

def list_articles(request):
    articles = Articles.objects.all()
    return render(request, 'home.html', {"articles": articles})

def article_detail(request, article_id):
    article = get_object_or_404(Articles, id=article_id)
    return render(request, 'article_detail.html', {"article": article})
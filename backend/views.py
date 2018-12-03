# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http  import HttpResponse

from . import models

# Create your views here.

def index(request):
    articles = models.Article.objects.all()
    return render(request, "backend/index.html", {'articles': articles})

def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, "backend/article_page.html", {'article': article})

def edit_page(request, article_id):
    if article_id == "0":
        return render(request, "backend/edit_page.html")
    article = models.Article.objects.get(pk=article_id)
    return render(request, "backend/edit_page.html", {'article': article})

def edit_action(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article_id = request.POST.get('article_id')
    if article_id == "0":
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, "backend/index.html", {'articles': articles})
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, "backend/article_page.html", {'article': article})

from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Article
#if you want to send HttpResponse or JsonResponse you should use the following commented code.
#from django.http import HttpResponse , JsonResponse
from django.http import Http404

def home (request):
    context = {
        "articles" : Article.objects.filter(status="p"),
    }
    return render (request, "blog/home.html", context)

def detail(request, slug):
    context = {
        #Article.objects.get (slug=slug)
        "article" : get_object_or_404 (Article, slug=slug, status = "p")
    }
    return render (request, "blog/detail.html", context)

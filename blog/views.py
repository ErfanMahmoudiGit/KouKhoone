from django.shortcuts import render
from .models import Article
#if you want to send HttpResponse or JsonResponse you should use the following commented code.
#from django.http import HttpResponse , JsonResponse

def home (request):
    context = {
        "articles" : Article.objects.filter(status="p"),
    }
    return render (request, "blog/home.html", context)

def detail(request, slug):
    context = {
        "article" : Article.objects.get (slug=slug)
    }
    return render (request, "blog/detail.html", context)

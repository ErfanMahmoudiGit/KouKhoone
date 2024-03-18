from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Article, category
#if you want to send HttpResponse or JsonResponse you should use the following commented code.
#from django.http import HttpResponse , JsonResponse
from django.http import Http404

def home (request):
    context = {
        # - means decending
        "articles" : Article.objects.filter(status="p").order_by('-publish'),
    }
    return render (request, "blog/home.html", context)

def detail(request, slug):
    context = {
        #Article.objects.get (slug=slug)
        "article" : get_object_or_404 (Article, slug=slug, status = "p"),
    }
    return render (request, "blog/detail.html", context)

def about (request):
    context = {
        # - means decending
        "articles" : Article.objects.filter(status="p").order_by('-publish'),
    }
    return render (request, "blog/about.html", context)

def contact (request):
    context = {
        # - means decending
        "articles" : Article.objects.filter(status="p").order_by('-publish'),
    }
    return render (request, "blog/contact.html", context)

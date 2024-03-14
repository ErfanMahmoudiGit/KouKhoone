from django.shortcuts import render
#from django.http import HttpResponse , JsonResponse
from .models import Article
# Create your views here.

def home (request):
    context = {
        "articles" : Article.objects.filter(status="p")
    }
    return render (request, "blog/home.html", context)
def greetings (request):
    return render (request, "blog/greetings.html")
def detail(request):
    pass

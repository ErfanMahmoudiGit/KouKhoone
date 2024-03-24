from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Article, category as categ
#if you want to send HttpResponse or JsonResponse you should use the following commented code.
#from django.http import HttpResponse , JsonResponse
from django.http import Http404
from django.core.paginator import Paginator

from django.views.generic.list import ListView
class ArticleList(ListView):
    #model= Article
    #context_object = "articles"
    template_name = "blog/home.html"
    queryset = Article.objects.filter(status="p").order_by('-publish')
    paginated_by = 6

"""
def home (request, page=1):
    articles_list = Article.objects.filter(status="p").order_by('-publish')
    paginator = Paginator(articles_list, 4)  # Show 25 contacts per page.
    #page_number = request.GET.get("page")
    articles = paginator.get_page(page)
    context = {
        # - means decending
        "articles" : articles,
    }
    return render (request, "blog/home.html", context)
"""

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

def category(request, slug, page=1):
    category = get_object_or_404 (categ, slug=slug, status = True)
    articles_list = category.articles.published()
    paginator = Paginator(articles_list, 4)  # Show 25 contacts per page.
    articles = paginator.get_page(page)


    context = {
        # - means decending
        "category" : category,
        "articles" : articles,
    }
    return render (request, "blog/category.html", context)

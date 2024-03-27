from blog.models import Article
from .serializers import ArticleSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

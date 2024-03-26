from blog.models import Article
from .serializers import ArticleSerializer
from rest_framework.generics import ListAPIView

class ArticleList(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

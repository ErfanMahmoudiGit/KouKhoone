from rest_framework import serializers
from blog.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        #fields = ("title","slug","author","category","description","thumbnail","publish","created","updated","status")
        #exclude ("created", "updated")

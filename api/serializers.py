from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        #fields = ("title","slug","author","category","description","thumbnail","publish","created","updated","status")
        #exclude ("created", "updated")
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"
        #fields = ("title","slug","author","category","description","thumbnail","publish","created","updated","status")
        #exclude ("created", "updated")

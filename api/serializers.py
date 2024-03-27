from rest_framework import serializers
from blog.models import Article
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        #fields = ("title","slug","author","category","description","thumbnail","publish","created","updated","status")
        #exclude ("created", "updated")
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        #fields = ("title","slug","author","category","description","thumbnail","publish","created","updated","status")
        #exclude ("created", "updated")

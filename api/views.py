from blog.models import Article
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import IsSuperUserOrStaffReadOnly, IsAuthorOrReadOnly, IsStaffOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.viewsets import ModelViewSet
class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)

"""
class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "slug"

    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)

class UserList(ListCreateAPIView):
    def get_queryset(self):
        print ("----------------------")
        print (self.request.user)
        print (self.request.auth)
        print ("----------------------")
        return User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly, )

class UserDetail(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly, )
"""
"""
#from rest_framework.views import APIView
#from rest_framework.response import Response
class RevokeToken (APIView):
    def get (self, request):
        return Response ({"method":"get not allowed. this api should be used to revoke a token."})

    def post (self, request):
        return Response ({"method":"post not allowed. this api should be used to revoke a token."})

    def put (self, request):
        return Response ({"method":"put not allowed. this api should be used to revoke a token."})

    def delete (self, request):
        request.auth.delete()
        return Response (status = 204)

    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )
"""

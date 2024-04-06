from blog.models import Article
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import IsSuperUserOrStaffReadOnly, IsAuthorOrReadOnly, IsStaffOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.viewsets import ModelViewSet

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "slug"

    """
    def get_queryset(self):
        queryset = Article.objects.all()

        status = self.request.query_params.get('status')
        if status is not None:
            queryset = queryset.filter(status = status)

        author = self.request.query_params.get('author')
        if author is not None:
            queryset = queryset.filter(author__username = author)

        return queryset
    """
    filterset_fields = ["status", "author"]

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]

class UserViewSet (ModelViewSet):
    def get_queryset(self):
        print ("----------------------")
        print (self.request.user)
        print (self.request.auth)
        print ("----------------------")
        return get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly, )

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

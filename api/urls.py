"""
from api.views import ArticleList, ArticleDetail, UserList, UserDetail
urlpatterns = [
    path ("", ArticleList.as_view(), name = "home"),
    path ("page/<int:page>", ArticleList.as_view(), name = "home"),
    path ("<int:pk>", ArticleDetail.as_view(), name = "detail"),
    path ("<slug:slug>", ArticleDetail.as_view(), name = "detail"),
    path ("users/", UserList.as_view(), name = "userlist"),
    path ("users/<int:pk>", UserDetail.as_view(), name = "userdetail"),
]
"""

from django.urls import path, include
from rest_framework import routers
from api.views import UserViewSet, ArticleViewSet

app_name = "api"

router = routers.SimpleRouter()
router.register('articles', ArticleViewSet, basename= 'articles')
router.register('users', UserViewSet, basename= 'users')

urlpatterns = [
    path ("", include(router.urls)),
]

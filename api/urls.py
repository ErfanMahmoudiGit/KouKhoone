from django.urls import path, include
from api.views import ArticleList, ArticleDetail, UserList, UserDetail

app_name = "api"
urlpatterns = [
    path ("", ArticleList.as_view(), name = "home"),
    path ("page/<int:page>", ArticleList.as_view(), name = "home"),
    path ("<int:pk>", ArticleDetail.as_view(), name = "detail"),
    path ("<slug:slug>", ArticleDetail.as_view(), name = "detail"),
    path ("users/", UserList.as_view(), name = "userlist"),
    path ("users/<int:pk>", UserDetail.as_view(), name = "userdetail"),
]

from django.urls import path, include
from api.views import ArticleList

app_name = "api"
urlpatterns = [
    path ("", ArticleList.as_view(), name = "home"),
    path ("page/<int:page>", ArticleList.as_view(), name = "home"),
]

from django.urls import path
from blog.views import home, greetings, detail

app_name = "blog"
urlpatterns = [
    path ("", home, name = "home"),
    path ("article/", detail, name = "detail"),
    path ("greetings/", greetings, name = "greetings"),

]

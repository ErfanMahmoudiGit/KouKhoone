from django.urls import path
from blog.views import home, detail, about, contact

app_name = "blog"
urlpatterns = [
    path ("", home, name = "home"),
    path ("article/<slug:slug>", detail, name = "detail"),
    path ("about", about, name = "about"),
    path ("contact", contact, name = "contact"),
]

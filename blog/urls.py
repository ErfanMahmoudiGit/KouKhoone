from django.urls import path
from blog.views import home, detail, about, contact, category

app_name = "blog"
urlpatterns = [
    path ("", home, name = "home"),
    path ("page/<int:page>", home, name = "home"),
    path ("article/<slug:slug>", detail, name = "detail"),
    path ("about", about, name = "about"),
    path ("contact", contact, name = "contact"),
    path ("category/<slug:slug>", category, name = "category"),
    path ("category/<slug:slug>/page/<int:page>", category, name = "category"),
]

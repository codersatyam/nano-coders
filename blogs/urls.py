from django.urls import path
from . import views
urlpatterns = [
    path("postcomments", views.postcomments, name="postcomments"),
    path("", views.home, name="home"),
    path("own_blogs", views.own_blogs, name="own_blogs"),
    path("make", views.make, name="make"),
    path("<str:slug>", views.content, name="content"),


    ]

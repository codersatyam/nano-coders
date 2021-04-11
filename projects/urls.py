from django.urls import path
from . import views
urlpatterns = [

    path("", views.index, name="index"),
    path("python", views.python, name="python"),
    path("c++", views.cplus, name="c++"),
    path("java", views.java, name="java"),
    path("p1", views.p1, name="p1"),
    path("p2", views.p2, name="p2"),
    path("p3", views.p3, name="p3"),
    path("p4", views.p4, name="p4"),
    path("p5", views.p5, name="p5"),
    path("p6", views.p6, name="p6"),
    path("p7", views.p7, name="p7"),
    path("p8", views.p8, name="p8"),
    path("p9", views.p9, name="p9"),
    path("p10", views.p10, name="p10"),
    path("p11", views.p11, name="p11"),
    path("p12", views.p12, name="p12"),
    ]

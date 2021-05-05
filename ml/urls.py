from django.urls import path, include
from .import views

urlpatterns=[
    path("",views.home,name="home"),
    path("p1",views.p1,name="p1"),
]
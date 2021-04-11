from django.urls import path
from . import views
urlpatterns = [

    path("", views.index, name="index"),
    path("moretutorials1", views.moretutorials1, name="moretutorials1"),
    path("moretutorials2", views.moretutorials2, name="moretutorials2"),
    path("moretutorials3", views.moretutorials3, name="moretutorials3"),
    path("moretutorials4", views.moretutorials4, name="moretutorials4"),
    path("htmldoc", views.htmldoc, name="htmldoc"),
   
    ]

from django.urls import path
from . import views
urlpatterns = [

    path("", views.buyhome, name="buyhome"),
    path("sensor", views.sensor, name="sensor")
    ]
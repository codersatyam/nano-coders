from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [

    path("", views.home, name="home1"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contactus"),
    path("tools/", views.tools, name="tools"),
    path("search", views.search, name="search"),
    path("signup", views.signup, name="signup"),
    path("login", views.handlelogin, name="handlelogin"),
    path("logout", views.handlelogout, name="handlelogout"),
    path("reset_password/", auth_views.PasswordResetView.as_view(template_name='home/reset.html'), name="reset_password"),
    path("reset_password/done/", auth_views.PasswordResetView.as_view(template_name='home/reset_done.html'), name="reset_password_done"),
    path("reset_password_confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='home/reset_confirm.html'), name="reset_password_done"),


    ]



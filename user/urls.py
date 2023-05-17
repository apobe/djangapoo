from django.contrib import admin
from django.urls import path,include
from . import views
app_name="user"
urlpatterns = [
    path("register/",views.register,name="register"),
    path("login/",views.login1,name="login"),
    path("logout/",views.logout1,name="logout"),
    
]
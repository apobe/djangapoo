from django.contrib import admin
from django.urls import path,include
from . import views
app_name="makaleler"
urlpatterns = [
    path("dashboard/",views.dashboard,name="dashboard"),
    path("addarticle/",views.addarticle,name="addarticle"),
    path("delete/<int:id>",views.delete,name="delete"),
    path("update/<int:id>",views.update,name="update"),
    path("detay/<int:id>",views.detay,name="detay"),
    path("",views.makaleler,name="makaleler"),
    path("detay/<int:id>",views.commnet,name="comment"),
]

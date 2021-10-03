from django.contrib import admin
from django.urls import path, include
from dracula import views

urlpatterns = [
    path('', views.index, name="home"),
    # path('index', views.index, name="home"),
    # path('about', views.about, name="about"),
    # path('drop1', views.drop1, name="drop1"),
    # path('drop2', views.drop2, name="drop2"),
    # path('drop3', views.drop3, name="drop3"),
    # path('drop4', views.drop4, name="drop4"),
    # path('login', views.login, name="login"),
    
]
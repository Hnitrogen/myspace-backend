from django.contrib import admin
from django.urls import path , include 
from .views import create_user 

urlpatterns = [
    path("register/",create_user)
]

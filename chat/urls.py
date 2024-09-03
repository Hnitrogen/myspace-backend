from django.contrib import admin
from django.urls import path , include 
from .views import index , index2 

urlpatterns = [
    path('chat/',index) , 
    path('chat/admin/',index2)
]

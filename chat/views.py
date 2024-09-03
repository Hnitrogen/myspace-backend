from django.shortcuts import render

def index(request):
    return render(request,"chat.html")

def index2(request): 
    return render(request,"adminAnswer.html")
    
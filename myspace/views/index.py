from django.shortcuts import render

# 返回打包的前端！！！
def index(request):
    return render(request, "index.html")

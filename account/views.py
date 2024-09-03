from django.contrib.auth.models import User
from django.http import JsonResponse

def create_user(request): 
    if request.method == 'POST': 
        data = request.POST 
        username = data.get('username')
        password = data.get('password')
        if User.objects.filter(username=username).exists():
            JsonResponse({'result':'valid method!'})
        else: 
            user = User.objects.create_user(username=username, password=password, email="", first_name="", last_name="")

    else: return JsonResponse({'result':'valid method!'})
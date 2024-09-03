from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from myspace.models.todo import TodoList
import json

@csrf_exempt 
def todoDelete(request):
    if request.method == 'GET': 
        return JsonResponse({'result':'This is Get'})

    elif request.method == 'POST':      
        data = json.loads(request.body)
        iid = data['code']

        p = TodoList.objects.get(id=iid) 
        p.delete()
        return JsonResponse({'result':'success'})

@csrf_exempt
def todoPost(request):
    if request.method == 'POST': 
        TodoList.objects.create(content=request.POST.get('content',''))
        return JsonResponse({'result':'success'})
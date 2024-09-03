from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count 
from django.http import JsonResponse

from myspace.models.Hack import HackerImage 
from myspace.serializers import HackSerializer

class HackerDetail(APIView):
    def get(self,request,pk): 
        p = HackerImage.objects.get(code_id=pk) 
        serializer = HackSerializer(p) 
        return Response(serializer.data)


class HackerAll(APIView):
    def get(self,request):
        imgs = HackerImage.objects.all()
        res = []    
        for img in imgs : 
            res.append(img.code_id)
        return JsonResponse(res,safe=False)
            
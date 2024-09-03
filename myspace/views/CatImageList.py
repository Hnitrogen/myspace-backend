from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count 

from myspace.models.CatImage import CatImage 
from myspace.serializers import CatImageSerializer
import random

class CatImageList(APIView):
    def get(self,request): 
        p = CatImage.objects.all() 
        serializer = CatImageSerializer(p,many=True) # 序列化p为JSON
        return Response(serializer.data) 

class CatImageRandom(APIView):
    def get_object(self, pk):
        try:
            return CatImage.objects.get(pk=pk)
        except CatImage.DoesNotExist:
            raise CatImage.objects.get(pk=4)

    # 随机返回一张图片
    def get(self, request, pk, format=None):
        cnt = CatImage.objects.count() 
        random_number = random.randint(7,cnt+7)

        p = self.get_object(random_number)
        serializer = CatImageSerializer(p)
        return Response(serializer.data)
            
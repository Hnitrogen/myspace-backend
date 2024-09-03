from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count 
from django.http import JsonResponse

from myspace.models.paste import Paste
from myspace.serializers import PasteSerializer

class PasteList(APIView):
    def get(self,request):
        p = Paste.objects.all() 
        serializer = PasteSerializer(p,many=True) 
        return Response(serializer.data)

    def post(self,request):
        content = request.POST.get('content')

        if content == '': 
            return Response({'result','content is empty!'})

        else: p = Paste.objects.create(
            title = request.POST.get('title'),
            author = request.POST.get('author'),
            content = request.POST.get('content','')
        )

        reback_id = p.id 

        return Response({
            'result': 'success',
            'reback_id': reback_id , 
        }) 

class PasteDetail(APIView):
    def get(self,request,pk): 
        p = Paste.objects.get(id=pk) 
        serializer = PasteSerializer(p) 
        return Response(serializer.data)